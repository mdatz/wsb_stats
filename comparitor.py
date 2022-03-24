import praw
import datetime
import string
from datetime import date
from psaw import PushshiftAPI
from stock_dictionary import create_stock_dictionary
from operator import itemgetter

#Create Dictionairies
stock_dict = create_stock_dictionary();
count_dict = dict();

#Initialize PRAW API and Pushshift API
reddit = praw.Reddit(client_id=process.env.REDDIT_ID, client_secret=process.env.REDDIT_SECRET, user_agent=process.env.REDDIT_USER);
api = PushshiftAPI(reddit);

#Get Current Date
currentDate = datetime.datetime.today();

#Create hour-minute range lists
hours = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23];
minutes = [00,10,20,30,40,50,59];

#loop variables
i=0;
j=1;

#Loop through hour-minute ranges and scrape posts
while i < len(hours):
    while j < len(minutes):    
        
        #Progress Output
        print("Checking Time Interval " + str(hours[i]) + ":" + str(minutes[j-1]) + " - " + str(hours[i]) + ":" + str(minutes[j]));

        #Create time interval
        startTime = int(datetime.datetime(currentDate.year,currentDate.month,currentDate.day,hours[i],minutes[j-1]).timestamp());
        endTime = int(datetime.datetime(currentDate.year,currentDate.month,currentDate.day,hours[i],minutes[j]).timestamp());
        
        #Get Posts for given time range
        posts = list(api.search_submissions(after=startTime,before=endTime,subreddit='WallStreetBets',filter=['url','title'],limit=1000));
        
        #Loop through Titles and Check for Keywords
        for item in posts:
            
            #Remove punctuation and split title string
            temp_string = item.title.translate(string.punctuation);
            keywords = temp_string.split();
            
            #Look for keywords in title
            for word in keywords:

                #Check if in Stock Dictionary
                if(stock_dict.get(word)):

                    #Increment Count if exists
                    if(count_dict.get(word)):
                        count_dict[word] += 1;
                    else:
                        count_dict[word] = 1;

        #Increment minute loop
        j += 1;
    
    #Increment hour loop / reset minute loop
    i += 1;
    j = 1;

#Create a sorted list of items from keyword dictionary
sorted_list = sorted(count_dict.items(), key=itemgetter(1), reverse=True);

#Save List to File
with open(str(currentDate.year)+'-'+str(currentDate.month)+'-'+str(currentDate.day)+'-keywords.txt', 'w') as text_file:
    for item in sorted_list:
        text_file.write("%s\n" % str(item));

#Display results
for item in sorted_list:
    print(item);


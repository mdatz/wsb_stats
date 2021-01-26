import praw
from stock_dictionary import create_stock_dictionary

stock_dict = create_stock_dictionary();
print("Enter a word, this will look up any matches to the NASDAQ/TSX/NYSE/AMX Listed company dictionary:");
search_word = input();

print(stock_dict.get(search_word));

#reddit = praw.Reddit(client_id='crsLoAgMmlD3yg', client_secret='dwuSqAXNPm-ek1aS8sY78KvRGWe5Bw', user_agent='mdatx-script');

#hot_posts = reddit.subreddit('WallStreetBets').hot(limit=100);
#for post in hot_posts:
#    print(post.title);


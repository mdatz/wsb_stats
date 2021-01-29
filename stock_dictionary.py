## stock_dictionary.py
## -----------------------------------------------------
## Script for Loading the all NASDAQ/TSX/AMEX/NYSE Listed 
## companies symbols & Keywords into a data 
## dictionary for better lookup. Will create the 
## list for the scraper to compare scraped text against.

def create_nasdaq_dictionary(dictionary):

    ## Load the Text File sourced from [eoddata.com/symbols.aspx]
    text_file = open("./Stock_Exchange_Listings/NASDAQ.txt","r");
    
    ## Read each line and add Symbol & Security name to the Dictionary
    for line in text_file:
        contents = line.split("\t");
        dictionary[contents[0]] = True;
        dictionary[contents[0].lower()] = True;
        dictionary["$"+contents[0]] = True;
        dictionary["$"+contents[0].lower()] = True;

        description = contents[1].split();
        for word in description:
            dictionary[word] = True;
            dictionary[word.lower()] = True;
            dictionary[word.upper()] = True;

def create_tsx_dictionary(dictionary):

    ## Load the Text File sourced from [eoddata.com/symbols.aspx]
    text_file = open("./Stock_Exchange_Listings/TSX.txt","r");
    
    ## Read each line and add Symbol & Security name to the Dictionary
    for line in text_file:
        contents = line.split("\t");
        dictionary[contents[0]] = True;
        dictionary[contents[0].replace(".TO","")] = True;
        dictionary[contents[0].lower()] = True;
        dictionary["$"+contents[0]] = True;
        dictionary["$"+contents[0].lower()] = True;

        description = contents[1].split();
        for word in description:
            dictionary[word] = True;
            dictionary[word.lower()] = True;
            dictionary[word.upper()] = True;

def create_amex_dictionary(dictionary):

    ## Load the Text File sourced from [eoddata.com/symbols.aspx]
    text_file = open("./Stock_Exchange_Listings/AMEX.txt","r");
    
    ## Read each line and add Symbol & Security name to the Dictionary
    for line in text_file:
        contents = line.split("\t");
        dictionary[contents[0]] = True;
        dictionary[contents[0].lower()] = True;
        dictionary["$"+contents[0]] = True;
        dictionary["$"+contents[0].lower()] = True;

        description = contents[1].split();
        for word in description:
            dictionary[word] = True;
            dictionary[word.lower()] = True;
            dictionary[word.upper()] = True;

    
def create_nyse_dictionary(dictionary):

    ## Load the Text File sourced from [eoddata.com/symbols.aspx]
    text_file = open("./Stock_Exchange_Listings/NYSE.txt","r");
    
    ## Read each line and add Symbol & Security name to the Dictionary
    for line in text_file:
        contents = line.split("\t");
        dictionary[contents[0]] = True;
        dictionary[contents[0].lower()] = True;
        dictionary["$"+contents[0]] = True;
        dictionary["$"+contents[0].lower()] = True;

        description = contents[1].split();
        for word in description:
            dictionary[word] = True;
            dictionary[word.lower()] = True;
            dictionary[word.upper()] = True;


def create_stock_dictionary():
    
    stock_dictionary = dict();
    create_nasdaq_dictionary(stock_dictionary);
    create_tsx_dictionary(stock_dictionary);
    create_amex_dictionary(stock_dictionary);
    create_nyse_dictionary(stock_dictionary);
    
    stock_dictionary['retard'] = True;
    stock_dictionary['Retard'] = True;
    stock_dictionary['autist'] = True;
    stock_dictionary['Autist'] = True;

    return stock_dictionary;

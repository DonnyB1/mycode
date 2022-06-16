#!/usr/bin/env python3

# important to structure the data in a way that's easy to grab values out of it
# this is a list of dictionaries; what's next is to add a new dictionary for every
# other zodiac sign
my_list_of_dict = [
                   {"years":["2011","1999","1987","1975","1963"], 
                    "sign":"Rabbit", 
                    "trait": "you are vigilant, witty, quick-minded, and ingenious"}
                  ]

def main(year):    
    # year = usr_date below
    # get the user's name
    usr_name = input("Please enter your name:\n>") 
    usr_name = usr_name.title()   

    # loop over the list of dictionaries
    for each_dict in my_list_of_dict:
        # each dictionary is returned as "each_dict"
        # check if the year entered is in the list of years for that sign
        if year in each_dict["years"]:
            # if it is, grab the sign and trait from that dictionary
            y= each_dict['sign']
            z= each_dict['trait']
    
    # put it all together by printing out those variables in an f-string :)
    print(f"{usr_name} your zodiac sign is {y}, which means {z}.")


# this is the first line that executes
usr_date = input("Please enter your birth year in YYYY format, e.g 2010:\n>")

# passes that date into the function above
main(usr_date)

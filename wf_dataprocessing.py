import numpy as np
import pandas as pd

__author__ = "Andy Nelson"
__date__ = "September 25, 2022"

from regex import Regex

__assignment = "SER*94: Homework 2 Q4 Programming"


def web_scrapping(url, classname):
    # Import Requests, Beautiful Soup
    import requests
    from bs4 import BeautifulSoup
    """
    :param url: URL for web scrapping
    :param classname:  classname string of the element with reviews
    :return: list 

    Request data for the url. 
    Create a soup (parse the html data).
    Manually: go to inspect element on the reviews and check the class of the element.
    Get and return the plain text (preferably in list format).
    """
    # TODO

    # Return the plain text (list)
    plays = []
    downs = []
    third = []
    r = requests.get(url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        for review in soup.findAll('h3'):
            # print(review.get_text().strip())
            downs.append(review.get_text().strip())
        for review in soup.findAll(class_=classname):
            # print(review.get_text().strip())
            plays.append(review.get_text().strip())
        for review in soup.findAll(class_='headline'):
            # print(review.get_text().strip())
            third.append(review.get_text().strip())

    return plays, downs, third


def preprocessing(plays, downs, third):
    # Import nltk - only use nltk library to perform all the following processing.
    import nltk
    import re
    """
    :param reviews: Reviews list
    :return: Dataframe with processed reviews

    Lower-case all words.
    Remove all punctuations.
    Remove stopwords. (Stopwords are the lists in the nltk library that are trivial and not relevant to the context/text.)
    Perform lemmatization on the data.
    """
    # TODO

    # print(reviews['review'].lower())
    play_count = 0
    down_count = 0
    analyze_downs = []
    analyze_plays = []
    for down in downs:
        if '4th' in down:
            # print("down:", downs[down_count-1])
            if downs[down_count -1] == '':
                if downs[down_count-2] == '':
                    analyze_downs.append(downs[down_count - 3])
                    # print("play:", plays[play_count-1])
                    analyze_plays.append(plays[play_count - 3])
                else:
                    analyze_downs.append(downs[down_count - 2])
                    # print("play:", plays[play_count-1])
                    analyze_plays.append(plays[play_count - 2])
                    # print("down:", downs[down_count])
            else:
                analyze_downs.append(downs[down_count - 1])
                # print("play:", plays[play_count-1])
                analyze_plays.append(plays[play_count - 1])
            # print("down:", downs[down_count])
            analyze_downs.append(downs[down_count])
            # print("play:", plays[play_count])
            analyze_plays.append(plays[play_count])
        if 'END QUARTER 2' in plays[play_count]:
            play_count += 1
        play_count += 1
        down_count += 1

    count = 0
    penguin = True
    while penguin:
        print("count is: ", count)
        if analyze_plays[count] == analyze_plays[count + 1]:
            print("error 2, removing", analyze_downs.pop(count))
            print("error 2, removing", analyze_plays.pop(count))
            print("error 2, removing", analyze_downs.pop(count))
            print("error 2, removing", analyze_plays.pop(count))
            count -= 1
            pass
        if count == len(analyze_plays) - 2:
            penguin = False;
        count += 1

    count = 0
    for thing in analyze_downs:
        print("Down", analyze_downs[count])
        print("Play", analyze_plays[count])
        count += 1

    # Return the dataframe with the processed data
    return None  # TODO


if __name__ == '__main__':
    # give your desired urls and classnames, preferably from yelp
    url1 = "https://www.espn.com/nfl/playbyplay/_/gameId/401437753"
    classname1 = "post-play"

    # Part 1
    review_list1 = web_scrapping(url1, classname1)
    # print('plays - count: ', len(review_list1[0]), review_list1[0])
    # print('downs - count: ', len(review_list1[1]), review_list1[1])
    # print('third - count: ', len(review_list1[2]), review_list1[2])

    # Create a pandas dataframe from array
    # df1 = pd.DataFrame(np.array(review_list1), columns=['post-play'])

    # Part 2
    processed_review1 = preprocessing(review_list1[0], review_list1[1], review_list1[2])

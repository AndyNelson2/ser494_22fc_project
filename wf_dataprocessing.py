import numpy as np
import pandas as pd

__author__ = "Andy Nelson"
__date__ = "Octcober 22, 2022"

__assignment = "SER*94: MS 3: Data Munging and Visualization"
data = []

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
        if count <= len(analyze_plays)-2:
            if analyze_plays[count] == analyze_plays[count + 1]:
                print("error 2, removing", analyze_downs.pop(count))
                print("error 2, removing", analyze_plays.pop(count))
                print("error 2, removing", analyze_downs.pop(count))
                print("error 2, removing", analyze_plays.pop(count))
                count -= 1
        if count >= len(analyze_plays)-1:
            penguin = False;
        count += 1

    count = 0
    penguin = True
    while penguin:
        print("count is: ", count)
        if '4th' in analyze_downs[count] and ('Field Goal' in analyze_plays[count] or 'kneels' in analyze_plays[count] or 'punts' in analyze_plays[count] or 'field goal' in analyze_plays[count]):
            print("error 3, removing", analyze_downs.pop(count))
            print("error 3, removing", analyze_plays.pop(count))
            print("error 3, removing", analyze_downs.pop(count-1))
            print("error 3, removing", analyze_plays.pop(count-1))
            count -= 1
        if count >= len(analyze_plays) - 1:
            penguin = False;
        count += 1

    count = 0
    while count < len(analyze_plays) - 1:
        play = [analyze_downs[count], analyze_plays[count], analyze_downs[count + 1], analyze_plays[count + 1]]
        data.append(play)
        #print(play)
        count += 2

    # Return the dataframe with the processed data
    return None  # TODO


if __name__ == '__main__':
    # give your desired urls and classnames, preferably from yelp
    url1 = "https://www.espn.com/nfl/playbyplay/_/gameId/40143"
    gameID = 7752
    url = url1 + str(gameID)
    classname1 = "post-play"

    for x in range(0,9):
        print("analyzing game", x)
        url = url1 + str(gameID + x)
        review_list1 = web_scrapping(url, classname1)
        processed_review1 = preprocessing(review_list1[0], review_list1[1], review_list1[2])
    for datum in data:
        print(datum)
    # Create a pandas dataframe from array
    # df1 = pd.DataFrame(np.array(review_list1), columns=['post-play'])

    # Part 2

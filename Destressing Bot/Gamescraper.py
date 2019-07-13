#Import requests, random, lxml and beautifulsoup modules
import requests
from bs4 import BeautifulSoup
import lxml
import random

#Create function to webscrape a game website and return the link to a game
def get_random_game():
    #Categories of games in the website
    Choices_gs = ["New/b48a4d59-c36a-411e-8fa1-0224fe0f01c0", "Best/702b9531-c136-437a-ab97-0b209d893b55", "Match-3/a0732787-677c-4ff9-9ef5-73a21ff26f64", "Bubble-Shooter/09a8f220-955e-4114-a189-175faa5f1374","Puzzle/af2ebd26-0786-423b-90da-ffb229840819", "Quiz/8e0b96cd-0fed-4354-a43d-ae4785a798fd","Cards/b32b5c79-362e-42a2-8a72-96f0ffe24bbb", "Girls/018103c4-e4a9-4b0e-86c1-5cc6782053ca","Jump-Run/8a2ce06d-c47f-4eec-8c0b-8d52e48072bb", "Arcade/ecfe76c8-13f9-49c1-b81a-084011512dba","Racing/b53dc097-05cd-457f-a811-e0c6c47ca37a", "Sport/92ab9ee5-0dc8-45b4-bf5a-517fc3de0caf"]
    #General URL to webscrape from
    url_gs = "http://html5games.com/"
    #Choose a random category of games and append it to the URL
    URL_gs = url_gs + random.choice(Choices_gs)
    #Gets the results from that specific URL
    response = requests.get(URL_gs)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    tags = soup.find_all('ul', {"class": "games"})
    Tags = tags[0].find_all('li')
    max_range_gs = len(Tags)
    #Choose a random game from the results
    back_url_gs = Tags[random.randint(0, max_range_gs)].a.get('href')
    game_url = url_gs + back_url_gs
    #Returns the link to that game
    return game_url
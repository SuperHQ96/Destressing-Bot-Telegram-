#Import requests, beautiful soup, lxml as well as random modules
import requests
from bs4 import BeautifulSoup
import lxml
import random

#Function to obtain a random photo from the web
def get_random_picture():
    #Define output2_ws, output_ws, description_ws as well as description2_ws as global variables. This is to be convenient to be used for the try-except later on
    global output_ws
    global description_ws
    global description2_ws
    global output2_ws
    #A list of choices which the bot can choose from
    choices = ["funny", "superhero", "video", "ask9gag", "gaming", "wtf", "savage", "gif", "movie-tv", "comic", "sport", "girly", "relationship", "awesome", "cute", "country", "school", "horror", "science", "imadedis", "politics", "timely", "girl", "anime-manga", "food"]
    #General URL
    url_ws = "https://9gag.com/"
    #Generate a specific url by appending a randomly selected path to the back of the general url.
    URL_ws = url_ws + random.choice(choices)
    #Obtain the information from the website
    response = requests.get(URL_ws)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    #Try-except is to handle the cases where there are no pictures on that particular website (the website may be updated over time). When this happens, the function will run again and the global variables of output2_ws, output_ws, description2_ws and description_ws will be redefined.
    try:
        #Generate a list of the information about the picture from the data from the website
        tags = soup.find_all('div', {"class": "badge-post-container post-container "})
        #Randomly select one picture
        Tag = random.choice(tags)
        #Obtain the url of the picture to download from
        output_ws = Tag.a.img.get("src")
        #Obtain the description of the image
        description_ws = Tag.a.img.get("alt")
    except:
        get_random_picture()
    #Try-except may redefine the global variables many times in this function. Therefore, output2_ws and description2_ws are assigned as the final value of output_ws and description_ws respectively.
    output2_ws = output_ws
    description2_ws = description_ws
    #Returns the description as well as the url of the image
    return description2_ws, output2_ws

#Function to obtain a randomly selected video
def get_random_video():
    #Define output2_ws and output_ws as global variables
    global output_ws
    global output2_ws
    #A list of choices of the various web pages to scrape from
    choices = ["funny", "superhero", "video", "ask9gag", "gaming", "wtf", "savage", "gif", "movie-tv", "comic", "sport",
               "girly", "relationship", "awesome", "cute", "country", "school", "horror", "science", "imadedis",
               "politics", "timely", "girl", "anime-manga", "food"]
    #General URL to scrape from
    url_ws = "https://9gag.com/"
    #Generate a a specific URL to scrape from by appending a randomly selected choice from the list to the back of the general URL
    URL_ws = url_ws + random.choice(choices)
    #Use the requests module to obtain the data from the web page
    response = requests.get(URL_ws)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    #Try-except is to handle the cases where there are no videos on that particular website (the website may be updated over time). When this happens, the function will run again and the global variables of output2_ws and output_ws will be redefined.
    try:
        #Find all mp4 videos
        tags = soup.find_all('source', {"type": "video/mp4"})
        #Randomly select one of them
        Tag = random.choice(tags)
        #Obtain the url to download the video from
        output_ws = Tag.get('src')
    except:
        get_random_video()
    #Try-except may redefine the global variables many times in this function. Therefore, output2_ws will be assigned to the final value of output_ws.
    output2_ws = output_ws
    #Returns the URL of the video
    return output2_ws
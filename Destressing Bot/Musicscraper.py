#Import requests, random, lxml and beautifulsoup modules
import requests
from bs4 import BeautifulSoup
import lxml
import random

# Create a function to webscrape for music
def get_music(genre):
    #Choosing the genres based on the user's selection
    if genre == "Classical":
        URL = "/charts/top?genre=classical&country=all-countries"
    if genre == "Dance & EDM":
        URL = "/charts/top?genre=danceedm&country=all-countries"
    if genre == "Electronic":
        URL = "/charts/top?genre=electronic&country=all-countries"
    if genre == "Hip-hop & Rap":
        URL = "/charts/top?genre=hiphoprap&country=all-countries"
    if genre == "House":
        URL = "/charts/top?genre=house&country=all-countries"
    if genre == "Indie":
        URL = "/charts/top?genre=indie&country=all-countries"
    if genre == "Jazz & Blues":
        URL = "/charts/top?genre=jazzblues&country=all-countries"
    if genre == "Metal":
        URL = "/charts/top?genre=metal&country=all-countries"
    if genre == "Piano":
        URL = "/charts/top?genre=piano&country=all-countries"
    if genre == "R&B & Soul":
        URL = "/charts/top?genre=rbsoul&country=all-countries"
    if genre == "Rock":
        URL = "/charts/top?genre=rock&country=all-countries"
    if genre == "Slow, calm music":
        URL = "/relaxdaily/slow-calm-music/recommended"
	#General url to search from
    url = "https://soundcloud.com"
	#Specific URL to webscrape from by appending to genre to the back of the main url
    URL_ms = url + URL
	#Gets the results from that specific URL
    response = requests.get(URL_ms)
    data = response.text
    soup = BeautifulSoup(data, 'lxml')
    tags = soup.find_all('h2', {'itemprop': 'name'})
	#Randomly select one of the music scraped from the website.
    Tag = random.choice(tags)
	#Gets the back portion of the url of that music
    back_url_ms = Tag.a.get('href')
	#Appends the back portion of the music to the main URL to obtain the actual URL of that music and returns it at the end
    music_url = url + back_url_ms
    return music_url

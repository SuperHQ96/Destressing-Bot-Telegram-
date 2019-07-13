#Import all the necessary modules, scripts and libraries
import telepot
import requests
import time
from telepot.loop import MessageLoop
import Gamescraper
import Funnyscraper
import Musicscraper
import random
import json
import xlrd
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

time_keeper = True

#Emojis used for telegram bot replies
back_emoji = u'\U0001F519'
sad_emoji = u'\U0001F622'
muscle_emoji = u'\U0001F4AA'
graduation_emoji = u'\U0001F393'
twohearts_emoji = u'\U0001F49E'
stop_emoji = u'\U0001F645'
coolface_emoji = u'\U0001F60E'
rainbow_emoji = u'\U0001F308'
worried_emoji = u'\U0001F61F'
radiant_emoji = u'\U0001F647'
music_emoji = u'\U0001F3B6'
monkey_emoji = u'\U0001F64A'
sparkle_emoji = u'\U00002728'
pray_emoji = u'\U0001F64F'
catlaugh_emoji = u'\U0001F639'
wink_emoji = u'\U0001F609'
sleepy_emoji = u'\U0001F634'
cycling_emoji = u'\U0001F6B5'
dog_emoji = u'\U0001F415'
whale_emoji = u'\U0001F433'
sunflower_emoji = u'\U0001F33C'
family_emoji = u'\U0001F46A'
guitar_emoji = u'\U0001F3BB'
icecream_emoji = u'\U0001F366'
question_emoji = u'\U00002753'
shy_emoji = u'\U0001F633'
front_face_chick_emoji = u'\U0001F425'
game_emoji = u'\U0001F3AE'

#Function to be used under callback query to return the helpline information from the spreadsheet. from_id is used as an argument so that both chat_id (for the command-handling function) as well as from_id (for the callback query-handling function) can be used
def get_helpline(row, format_id):
    #Extracting the type of helpline, the organisation, the details of the helpline, the helpline number as well as the operating hours using the helpline function
    type_help, organisation_help, details_help, helpline_number_help, operating_hours_help = helpline(row)
    #Send the information back to the user
    bot.sendMessage(format_id, organisation_help)
    bot.sendMessage(format_id, details_help)
    bot.sendMessage(format_id, helpline_number_help)
    bot.sendMessage(format_id, operating_hours_help)

#Function to extract data from Excel spreadsheet file
def helpline(row):
    #Spreadsheet we are extracting data from
    workbook = xlrd.open_workbook('helplines.xlsx')
    worksheet = workbook.sheet_by_index(0)
    #Assigning variables to each column in the row
    type, organisation, details, helpline_number, operating_hours = worksheet.row_values(row)
    #Return the variables
    return type,organisation,details,helpline_number,operating_hours

#Function to handle commands
def on_chat_message(msg):
    #Obtain the information of the message of the user using telepot.glance
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        msg_text = msg['text']
        #If message is a command in telegram
        if (msg_text.startswith('/')):
            command = msg_text[1:].lower()
            #Returns description of the bot
            if command == ('about'):
                bot.sendMessage(chat_id, "This bot is meant to help you de-stress after a long tiring day of work, school or studying for exams!" + sleepy_emoji)
                bot.sendMessage(chat_id, "Just use the menu beside the message bar to use the function of this bot, or type / to see a list of commands.\n\nWe hope this bot can cheer you up and remind you that whatever problems you are facing are always temporary, there's so much more to life that makes it worth living for " + sunflower_emoji + whale_emoji + family_emoji + icecream_emoji)
            #Returns a funny photo or gif/video
            if command == ('funny'):
                confirm_keyboard = InlineKeyboardMarkup(
                    inline_keyboard=[[InlineKeyboardButton(text='Picture', callback_data='funny-picture')],
                                     [InlineKeyboardButton(text='Video', callback_data='funny-video')]])
                bot.sendMessage(chat_id, "Would you like a picture or a video to go with that order?", reply_markup=confirm_keyboard)
            #Returns an inspirational quote
            if command == ('quote'):
                global time_keeper
                # It can only return a result every 6 minutes
                if time_keeper == True or time.time() - time_keeper >= 6 * 60:
                    bot.sendMessage(chat_id, "Here's a little magic to get you all pumped up or enlightened" + front_face_chick_emoji + ":")
                    Choices_iq = ['life', 'inspire', 'management', 'sports', 'funny', 'love', 'art', 'students']
                    Choice_iq = random.choice(Choices_iq)
                    url_iq = "http://quotes.rest/qod.json?category=" + Choice_iq
                    response = requests.get(url_iq).json()
                    bot.sendMessage(chat_id, response["contents"]["quotes"][0]["quote"])
                    time_keeper = time.time()
                elif time.time() - time_keeper < 6 * 60:
                    bot.sendMessage(chat_id,"Sorry, but we're a little short on pixie dust now (they provide the magic to our quotes). Please try again after 6 minutes!")
            #Returns a custom menu displaying the different categories for the helplines
            if command == ('helpline'):
                type_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Suicide',callback_data='sui')],[InlineKeyboardButton(text='Addiction',callback_data='add')],[InlineKeyboardButton(text='Youth',callback_data='youth')],[InlineKeyboardButton(text='Counselling',callback_data='cou')],[InlineKeyboardButton(text='Child abuse',callback_data='child')],[InlineKeyboardButton(text='Family violence',callback_data='fam')],[InlineKeyboardButton(text='Gambling',callback_data='gamb')],[InlineKeyboardButton(text='Mental health',callback_data='menh')],[InlineKeyboardButton(text='University',callback_data='uni')]])
                bot.sendMessage(chat_id,"Which type of helpline are you looking for my dear" + question_emoji,reply_markup=type_keyboard)
            #Returns a link to a fun game
            if command == ('game'):
                bot.sendMessage(chat_id, "I'm sure this game will get you all hyped up! " + game_emoji)
                bot.sendMessage(chat_id,Gamescraper.get_random_game())
            #Returns a music
            if command == ('music'):
                confirm_keyboard = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Classical',callback_data='music-class')], [InlineKeyboardButton(text='Dance & EDM',callback_data='music-daedm')], [InlineKeyboardButton(text='Electronic',callback_data='music-elec')], [InlineKeyboardButton(text='Hip-hop & Rap',callback_data='music-hhar')], [InlineKeyboardButton(text='House',callback_data='music-house')], [InlineKeyboardButton(text='Indie',callback_data='music-indie')], [InlineKeyboardButton(text='Jazz & Blues',callback_data='music-jab')], [InlineKeyboardButton(text='Metal',callback_data='music-metal')], [InlineKeyboardButton(text='Piano',callback_data='music-piano')], [InlineKeyboardButton(text='R&B & Soul',callback_data='music-rabas')], [InlineKeyboardButton(text='Rock',callback_data='music-rock')], [InlineKeyboardButton(text='Slow and calm',callback_data='music-scm')]])
                bot.sendMessage(chat_id, "Which genre of music would you like to indulge in, good Sir/Madam? " + music_emoji,reply_markup=confirm_keyboard)

#Function to handle inline keyboard queries
def on_callback_query(msg):
    #Obtain the information of queries from inline keyboards with the flavor 'callback_query' using telepot.glance
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    inline_message_id = msg['message']['chat']['id'], msg['message']['message_id']
    #The fllowing are the handle the various callback queries. bot.editMessageReplyMarkup is to remove the inline keyboard each time a query is made. A customised reply for each query is also sent back to the user each time the user makes a query to make the bot more human-like
    if (query_data == 'sui'):
        get_helpline(0,from_id)
        bot.sendMessage(from_id,"It doesn't have to end this way. The world needs you, we need you " + sad_emoji)
    if (query_data == 'add'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='National Addictions Management Service (NAMS)', callback_data='org-nams')],[InlineKeyboardButton(text='Alcoholics Anonymous', callback_data='org-aa')],[InlineKeyboardButton(text='Go Back ' + back_emoji, callback_data='goback')]]))
    if (query_data == 'youth'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='eCounselling Centre (eC2)', callback_data='org-ec2')], [InlineKeyboardButton(text='MeToYou Cyber Care',callback_data='org-m2y')],[InlineKeyboardButton(text='Go Back ' + back_emoji, callback_data='goback')]]))
    if (query_data == 'cou'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Counselling and Care Centre', callback_data='org-ccc')],[InlineKeyboardButton(text='WINGS Counselling Centre',callback_data='org-wcc')],[InlineKeyboardButton(text='Go Back ' + back_emoji, callback_data='goback')]]))
    if (query_data == 'child'):
        get_helpline(7,from_id)
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text="Don't be afraid to speak up, every child is precious " + twohearts_emoji)
    if (query_data == 'fam'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='TRANS SAFE Centre', callback_data='org-tsc')],[InlineKeyboardButton(text='Care Corner Project START', callback_data='org-ccps')],[InlineKeyboardButton(text='Go Back ' + back_emoji, callback_data='goback')]]))
    if (query_data == 'gamb'):
        get_helpline(10,from_id)
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text="It's never too late to quit " + muscle_emoji)
    if (query_data == 'menh'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Singapore Association for Mental Health (SAMH) Helpline', callback_data='org-samh')], [InlineKeyboardButton(text='IMH Helpline', callback_data='org-imh')], [InlineKeyboardButton(text='YouthReach Centre, Singapore Association of Mental Health (SAMH)', callback_data='org-samh2')],[InlineKeyboardButton(text='Go Back ' + back_emoji, callback_data='goback')]]))
    #This go back button is for those who wants to return to the type menu after selecting a type of organisation
    if (query_data == 'goback'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text='*Suicide', callback_data='sui')],
                             [InlineKeyboardButton(text='*Addiction', callback_data='add')],
                             [InlineKeyboardButton(text='*Youth', callback_data='youth')],
                             [InlineKeyboardButton(text='*Counselling', callback_data='cou')],
                             [InlineKeyboardButton(text='*Child abuse', callback_data='child')],
                             [InlineKeyboardButton(text='*Family violence', callback_data='fam')],
                             [InlineKeyboardButton(text='*Gambling', callback_data='gamb')],
                             [InlineKeyboardButton(text='*Mental health', callback_data='menh')],
                             [InlineKeyboardButton(text='*University', callback_data='uni')]]))
    if (query_data == 'uni'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='NUS', callback_data='org-nus')], [InlineKeyboardButton(text='NTU',callback_data='org-ntu')],[InlineKeyboardButton(text='SMU',callback_data='org-smu')], [InlineKeyboardButton(text='SIM',callback_data='org-sim')],[InlineKeyboardButton(text='Go Back ' + back_emoji, callback_data='goback')]]))
    if (query_data == 'org-nams'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(1,from_id)
        bot.sendMessage(from_id, text="It's not too late to stop now " + stop_emoji)
    if (query_data == 'org-aa'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(2,from_id)
        bot.sendMessage(from_id, text="It's not too late to stop now " + stop_emoji)
    if (query_data == 'org-ec2'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(3,from_id)
        bot.sendMessage(from_id, text="Everything is better when you have someone to talk to " + coolface_emoji)
    if (query_data == 'org-m2y'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(4,from_id)
        bot.sendMessage(from_id, text="Everything is better when you have someone to talk to " + coolface_emoji)
    if (query_data == 'org-ccc'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(5,from_id)
        bot.sendMessage(from_id, text="There's no problem in this world that can't be solved " + rainbow_emoji)
    if (query_data == 'org-wcc'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(6,from_id)
        bot.sendMessage(from_id, text="There's no problem in this world that can't be solved " + rainbow_emoji)
    if (query_data == 'org-tsc'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(8,from_id)
        bot.sendMessage(from_id, text="Abuse and violence is not cool. Stop such acts today " + worried_emoji)
    if (query_data == 'org-ccps'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(9,from_id)
        bot.sendMessage(from_id, text="Abuse and violence is not cool. Stop such acts today " + worried_emoji)
    if (query_data == 'org-samh'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(11,from_id)
        bot.sendMessage(from_id, text="Take care of your health before taking care of others " + radiant_emoji)
    if (query_data == 'org-imh'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(12,from_id)
        bot.sendMessage(from_id, text="Take care of your health before taking care of others " + radiant_emoji)
    if (query_data == 'org-samh2'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(13,from_id)
        bot.sendMessage(from_id, text="Take care of your health before taking care of others " + radiant_emoji)
    if (query_data == 'org-nus'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(14,from_id)
        bot.sendMessage(from_id, text="You've come so far, don't give up now! " + graduation_emoji)
    if (query_data == 'org-ntu'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(15,from_id)
        bot.sendMessage(from_id, text="You've come so far, don't give up now! " + graduation_emoji)
    if (query_data == 'org-smu'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(16,from_id)
        bot.sendMessage(from_id, text="You've come so far, don't give up now! " + graduation_emoji)
    if (query_data == 'org-sim'):
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        get_helpline(17,from_id)
        bot.sendMessage(from_id, text="You've come so far, don't give up now! " + graduation_emoji)
    if (query_data == 'music-class'):
        bot.sendMessage(from_id, Musicscraper.get_music("Classical"))
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text="Here's a tiny dose of the classics!")
    if (query_data == 'music-daedm'):
        bot.sendMessage(from_id, Musicscraper.get_music("Dance & EDM"))
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text="This music will surely get you pumped up. Now break out those dance moves!")
    if (query_data == 'music-elec'):
        bot.sendMessage(from_id, Musicscraper.get_music("Electronic"))
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text='Have a taste of good ol\' electronics!')
    if (query_data == 'music-hhar'):
        bot.sendMessage(from_id, Musicscraper.get_music("Hip-hop & Rap"))
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text='Drop da beat!')
    if (query_data == 'music-house'):
        bot.sendMessage(from_id, Musicscraper.get_music("House"))
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text='Get down and party!')
    if (query_data == 'music-indie'):
        bot.sendMessage(from_id, Musicscraper.get_music("Indie"))
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text="For those who care more about music than popularity.")
    if (query_data == 'music-jab'):
        bot.sendMessage(from_id, Musicscraper.get_music("Jazz & Blues"))
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text='Music to soothe and relax your nerves.')
    if (query_data == 'music-metal'):
        bot.sendMessage(from_id, Musicscraper.get_music("Metal"))
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text='For all the headbangers out there!')
    if (query_data == 'music-piano'):
        bot.sendMessage(from_id, Musicscraper.get_music("Piano"))
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text='Where words fail, music speaks.')
    if (query_data == 'music-rabas'):
        bot.sendMessage(from_id, Musicscraper.get_music("R&B & Soul"))
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text="One good thing about music: when it hits you, you feel no pain.")
    if (query_data == 'music-rock'):
        bot.sendMessage(from_id, Musicscraper.get_music("Rock"))
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text="Let's rock this moment with love!")
    if (query_data == 'music-scm'):
        bot.sendMessage(from_id, Musicscraper.get_music("Slow, calm music"))
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, text='Here you goooozzzzzzzzzzz.....')
    if (query_data == 'funny-picture'):
        description_fun,url_fun = Funnyscraper.get_random_picture()
        bot.sendMessage(from_id, "Hope I manage to get you giggling!!!"+ wink_emoji)
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendMessage(from_id, description_fun)
        bot.sendChatAction(from_id, "upload_photo")
        bot.sendPhoto(from_id, url_fun)
    if (query_data == 'funny-video'):
        bot.sendMessage(from_id, "Fetching a laugh potion from Santa's bag...Hope it tickles your funny bones!! " + wink_emoji)
        bot.editMessageReplyMarkup(inline_message_id, reply_markup=None)
        bot.sendChatAction(from_id,"upload_video")
        bot.sendVideo(from_id, Funnyscraper.get_random_video())

#Define the token of the bot that is obtained from BotFather
TOKEN = '#Insert token here'

#Use the telepot function to interact with the telegram bot API
bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message, 'callback_query': on_callback_query}).run_as_thread()

#Keep the code running
while True:
    time.sleep(30)




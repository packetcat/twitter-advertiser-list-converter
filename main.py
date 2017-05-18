# Project name - twitter-advertiser-list-converter
# Author - staticsafe
# Purpose - Converts Twitter provided advertiser list PDF to a CSV file of user-ids that can be imported as a blocklist.
# Editorial - Use Mastodon instead.

import PyPDF2
import twitter
import time
import argparse

# Command line argument parsing
parser = argparse.ArgumentParser(description='Converts Twitter provided advertiser list PDF->CSV file of UIDs.')
parser.add_argument('-i', dest='inputpdf', type=str, help='PDF input file', default='twitter_advertiser_list.pdf')
parser.add_argument('-o', dest='outputcsv', type=str, help='CSV output file', default='advertisers.csv')
args = parser.parse_args()

# Create the PDF file object
pdfFileObj = open(args.inputpdf, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numberOfPages = pdfReader.getNumPages()
pageObj = []
userpages = []

# Iterate through each page in PDF and then make a list of unmodified users
for pages in range(numberOfPages):
    pageObj.append(pdfReader.getPage(pages))
    userpages.append(pageObj[pages].extractText())

# Iterate through the userpages list and create another list
extractedusers = []

for users in range(len(userpages)):
    extractedusers.append(userpages[users].split("@"))

# Clean up and write file of users

# Loop to write users list into file
finaluserslist = open('users.txt', 'w')
for items in extractedusers:
    finaluserslist.write("\n".join(items))
finaluserslist.close()

# We need all the lines for some cleanup
finaluserslist = open('users.txt', 'r')
lines = finaluserslist.readlines()
finaluserslist.close()

# Cleanup extraneous text before writing the final file
finaluserslist = open('users.txt', 'w')
for line in lines:
    if line != "Your Twitter Advertisers"+"\n":
        finaluserslist.write(line)
finaluserslist.close()

# Now for the Twitter stuff
# Dictionary for Twitter OAuth credentials
oauth = {
    'ACCESS_TOKEN_KEY': '',
    'ACCESS_TOKEN_SECRET': '',
    'CONSUMER_KEY': '',
    'CONSUMER_SECRET': '',
}

# Instantiate Twitter API
api = twitter.Api(consumer_key=oauth['CONSUMER_KEY'], consumer_secret=oauth['CONSUMER_SECRET'], access_token_key=oauth['ACCESS_TOKEN_KEY'], access_token_secret=oauth['ACCESS_TOKEN_SECRET'])

# Make list of users
users = [line.strip() for line in open("users.txt").readlines()]
# Open file handle for the CSV we need
ids = open(args.outputcsv, 'w')

# Loop that gets the user ID of each user and writes it to the CSV
for user in users:
    try:
        userdata = api.GetUser(screen_name=user)
    except twitter.error.TwitterError as e:
        print("Unable to get user {}: {}".format(user, e))
        time.sleep(1)
        continue
    id = str(userdata.id)
    print(id)
    ids.write(id + "\n")
    time.sleep(1)
ids.write("\b")
ids.close()

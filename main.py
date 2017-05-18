# Project name - twitter-advertiser-list-converter
# Author - staticsafe
# Purpose - Converts Twitter provided advertiser list PDF to a CSV file of user-ids that can be imported as a blocklist.
# Editorial - Use Mastodon instead.

import PyPDF2

pdfFileObj = open('C:\\Users\\sadiq\\Downloads\\temp\\twitter_advertiser_list.pdf', 'rb')
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

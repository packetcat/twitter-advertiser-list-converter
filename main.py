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

#stringofusers = str(extractedusers)

#print(stringofusers)

#print("\n".join(stringofusers.split(',')))

# ARCHIVED

PROBABLY BROKEN SO ARCHIVING THIS.

# twitter-advertiser-list-converter
Converts Twitter provided advertiser list PDF to a CSV file of user-ids that can be imported as a blocklist.

## System requirements

- Python 3.x (I tested this on Python 3.6.1.)

### Python modules

You can install these via pip.

- PyPDF2
- python-twitter

## Twitter API key requirements
To use this script you will need a set of Twitter API credentials.

This can be obtained via [Twitter Application Management](https://apps.twitter.com/).

## Input file requirements
To use this script you will need a PDF list of your Twitter advertisers.

This can be obtained from Twitter themselves like so:
1. Log into your Twitter account via twitter.com.
2. Click on the user icon to the left of the "Tweet" button.
3. Click on "Settings and privacy".
4. Click on "Your Twitter data".
5. Twitter will ask you to confirm your password, do so.
6. Scroll to the bottom of the page, click a button marked "Request advertiser list" under the header "Tailored audiences".
7. Twitter will generate the PDF file and e-mail it to the e-mail address associated with your Twitter account.
8. Download said PDF file from the e-mail sent.
9. Use said PDF file with this script.

## Output file usage
This script outputs a new-line delimited file that can be imported via Twitter's blacklist import functionality.

This is how you do that:
1. Log into your Twitter account via twitter.com.
2. Click on the user icon to the left of the "Tweet" button.
3. Click on "Settings and privacy".
4. Click on "Blocked accounts".
5. Click on "Advanced options".
6. Click on "Import a list".
7. Attach the script generated file and preview it before you follow through.

## Need help?
If you need help or run into issues running this script, please open a GitHub issue and I will try to help you.

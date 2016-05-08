"""Script for broadcasting an SMS to a list of numbers."""
import csv
from twilio.rest import TwilioRestClient

# These are your Twilio API credentials
account = 'XXXXXXXXXXXXXXXXXXXXXXXX'
token = 'XXXXXXXXXXXXXXXXXXXXXXXX'

# This is the Twilio number that you are sending the SMS from
fromno = '4407xxxxxxxxx'

# This is the text you would like in the SMS
body = 'xxxxxxxx Put your message here xxxxxxxx'

# This is the CSV file containing a list of mobile numbers
# to which you want to broadcast the SMS
csv_file_name = 'numbers.csv'

# Create the Twilio Client to send the SMS messages
client = TwilioRestClient(account, token)

# Open the CSV, work through the rows and send the SMS to each number in the list
with open(csv_file_name) as file:
    reader = csv.reader(file)

    for row in reader:
       try:
            message = client.messages.create(to=row[0],
                                             from_=fromno,
                                             body=body)
            print(str.format('Sent message to {0}', row[0]))

        except:
            print(str.format('Unable to send message to {0}', row[0]))

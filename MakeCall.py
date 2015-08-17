# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
import config

# Get these credentials from http://twilio.com/user/account
account_sid = config.account_sid
auth_token = config.auth_token
client = TwilioRestClient(account_sid, auth_token)
from_number = config.from_number
to_number = config.to_number
url = "http://twimlets.com/menu?Message=Hello.%20Please%20press%201%20to%20listen%20to%20Ambient%20Music.&Options%5B1%5D=http%3A%2F%2Ftwimlets.com%2Fholdmusic%3FBucket%3Dcom.twilio.music.ambient&"

# Make the call
call = client.calls.create(to=to_number,  # Any phone number
                           from_=from_number, # Must be a valid Twilio number
                           url=url)
print(call.sid)

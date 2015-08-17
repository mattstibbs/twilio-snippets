# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Get these credentials from http://twilio.com/user/account
account_sid = "Axxxxxxxxxxxxxxxx"
auth_token = "xxxxxxxxxxxxxxxxxx"
client = TwilioRestClient(account_sid, auth_token)

# Make the call
call = client.calls.create(to="+447777111222",  # Any phone number
                           from_="+441111222333", # Must be a valid Twilio number
                           url="http://twimlets.com/menu?Message=Hello.%20Please%20press%201%20to%20listen%20to%20Ambient%20Music.&Options%5B1%5D=http%3A%2F%2Ftwimlets.com%2Fholdmusic%3FBucket%3Dcom.twilio.music.ambient&")
print(call.sid)

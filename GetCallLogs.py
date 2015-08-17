from twilio.rest import TwilioRestClient
import config

# To find these visit https://www.twilio.com/user/account
account_sid = config.account_sid
auth_token = config.auth_token

client = TwilioRestClient(account_sid, auth_token)

for call in client.calls.list():
    print("From: " + call.from_formatted + " To: " + call.to_formatted)

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACfef604e12269da11bfd56fcbf517adf6"
# Your Auth Token from twilio.com/console
auth_token  = "a9770946ca17680a3114083c9fa27097"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19497019690", 
    from_="+14083354483",
    body="Lena, are you there?")

print(message.sid)

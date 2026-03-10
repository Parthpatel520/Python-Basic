from twilio.rest import Client

account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"

client = Client(account_sid, auth_token)

message = client.messages.create(
    body="""Hello Mr. Kunj Chhatrala!

If you are currently working, please reply with Code 1.
If you are watching Instagram reels, please switch off your phone.

- Parth Chhatrala.
""",
    from_="+17752627678",
    to="+919106467043"
)

print("SMS Sent:", message.sid)
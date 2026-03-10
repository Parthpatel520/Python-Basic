from twilio.rest import Client

account_sid = "ACaa01dd0e45663f822ce483a24e6a2490"
auth_token = "d1a70d59807469ed82c694276835d58d"

client = Client(account_sid, auth_token)

message = client.messages.create(
      body="""Hello Mr. Kunj Chhatrala!,
      
        If you are currently working, please reply with Code 1.
        If you are watching Instagram reels, please switch off your phone.
          - Parth Chhatrala.""",
        
    from_="+1 775 262 7678",     # Twilio number
    to="+919106467043"       # Your number
)

print("SMS Sent:", message.sid)


# twilio = MQ9K8SEDBAYCVCQX5Q7Z3M19


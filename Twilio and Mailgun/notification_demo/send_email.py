import requests

otp = 501213

api_key = "bd29cb1ea176ef17fa83885fbed45d42-c6620443-77d27f78"
domain = "sandboxa0bd74d1af854b808b9be1c48f11d37d.mailgun.org"

response = requests.post(
    f"https://api.mailgun.net/v3/{domain}/messages",
    auth=("api", api_key),
    data={
        "from": f"OTP Service <mailgun@{domain}>",
        "to": "parthchhtrala@gmail.com",
        "subject": "Your OTP Code",
        "text": f"Your OTP is: {otp}"
    }
)

print("Email Status:", response.status_code)
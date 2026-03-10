# notification_demo (Twilio SMS + Mailgun Email)

Two small Python scripts:

- `send_sms.py`: sends an SMS via Twilio
- `send_email.py`: sends an email (OTP) via Mailgun

## Setup

1. Create a virtualenv and install deps:

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
pip install -r requirements.txt
```

2. Set environment variables (PowerShell examples):

```powershell
# Twilio
$env:TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
$env:TWILIO_AUTH_TOKEN="your_auth_token"
$env:TWILIO_FROM_NUMBER="+1xxxxxxxxxx"
$env:TWILIO_TO_NUMBER="+91xxxxxxxxxx"

# Mailgun
$env:MAILGUN_API_KEY="key-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
$env:MAILGUN_DOMAIN="sandboxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.mailgun.org"
$env:MAILGUN_TO_EMAIL="you@example.com"
# optional
$env:MAILGUN_FROM_EMAIL="OTP Service <mailgun@sandboxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.mailgun.org>"
```

## Send SMS (Twilio)

Uses CLI args first, then env vars.

```powershell
python .\\send_sms.py --to "+91xxxxxxxxxx" --from "+1xxxxxxxxxx" --body "Hello from Twilio"
```

Or rely on env vars:

```powershell
python .\\send_sms.py
```

## Send Email (Mailgun)

If you do not pass `--otp`, a random 6-digit OTP is generated.

```powershell
python .\\send_email.py --to "you@example.com" --subject "Your OTP Code" --otp 123456
```

Or rely on env vars:

```powershell
python .\\send_email.py
```

## Notes

- These scripts intentionally do not store credentials in code. Use env vars or CLI args.
- For Mailgun sandbox domains, the recipient often must be an authorized recipient in Mailgun.


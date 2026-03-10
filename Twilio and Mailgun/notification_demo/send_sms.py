import argparse
import os
import sys
from typing import Optional

from twilio.rest import Client


def _required(value: Optional[str], env_name: str) -> str:
    if value:
        return value
    env_value = os.getenv(env_name)
    if env_value:
        return env_value
    raise KeyError(env_name)


def main() -> int:
    parser = argparse.ArgumentParser(description="Send an SMS using Twilio.")
    parser.add_argument("--account-sid", help="Twilio Account SID (or TWILIO_ACCOUNT_SID).")
    parser.add_argument("--auth-token", help="Twilio Auth Token (or TWILIO_AUTH_TOKEN).")
    parser.add_argument("--from", dest="from_number", help="Twilio 'from' number (or TWILIO_FROM_NUMBER).")
    parser.add_argument("--to", dest="to_number", help="Recipient number (or TWILIO_TO_NUMBER).")
    parser.add_argument("--body", help="SMS body (or SMS_BODY).")
    args = parser.parse_args()

    try:
        account_sid = _required(args.account_sid, "TWILIO_ACCOUNT_SID").strip()
        auth_token = _required(args.auth_token, "TWILIO_AUTH_TOKEN").strip()
        from_number = _required(args.from_number, "TWILIO_FROM_NUMBER").strip()
        to_number = _required(args.to_number, "TWILIO_TO_NUMBER").strip()
    except KeyError as exc:
        missing = str(exc).strip("'")
        print(f"Missing required config: {missing}", file=sys.stderr)
        print("Set env vars or pass CLI args. See README.md.", file=sys.stderr)
        return 2

    body = (args.body or os.getenv("SMS_BODY") or "Hello from Twilio!").strip()

    client = Client(account_sid, auth_token)
    message = client.messages.create(body=body, from_=from_number, to=to_number)
    print("SMS Sent:", message.sid)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

import argparse
import os
import secrets
import sys
from typing import Optional

import requests


def _required(value: Optional[str], env_name: str) -> str:
    if value:
        return value
    env_value = os.getenv(env_name)
    if env_value:
        return env_value
    raise KeyError(env_name)


def _generate_otp() -> str:
    # 6-digit OTP, leading zeros allowed.
    return f"{secrets.randbelow(1_000_000):06d}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Send an email (OTP) using Mailgun.")
    parser.add_argument("--api-key", help="Mailgun API key (or MAILGUN_API_KEY).")
    parser.add_argument("--domain", help="Mailgun domain (or MAILGUN_DOMAIN).")
    parser.add_argument("--to", dest="to_email", help="Recipient email (or MAILGUN_TO_EMAIL).")
    parser.add_argument("--from", dest="from_email", help="From header (or MAILGUN_FROM_EMAIL).")
    parser.add_argument("--subject", default="Your OTP Code", help="Email subject.")
    parser.add_argument("--otp", help="OTP value (default: random 6-digit).")
    parser.add_argument("--text", help="Raw text body (overrides --otp).")
    args = parser.parse_args()

    try:
        api_key = _required(args.api_key, "MAILGUN_API_KEY").strip()
        domain = _required(args.domain, "MAILGUN_DOMAIN").strip()
        to_email = _required(args.to_email, "MAILGUN_TO_EMAIL").strip()
    except KeyError as exc:
        missing = str(exc).strip("'")
        print(f"Missing required config: {missing}", file=sys.stderr)
        print("Set env vars or pass CLI args. See README.md.", file=sys.stderr)
        return 2

    from_email = (args.from_email or os.getenv("MAILGUN_FROM_EMAIL") or f"OTP Service <mailgun@{domain}>").strip()
    otp = (args.otp or os.getenv("OTP") or _generate_otp()).strip()
    text = (args.text or os.getenv("MAILGUN_TEXT") or f"Your OTP is: {otp}").strip()

    response = requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={"from": from_email, "to": to_email, "subject": args.subject, "text": text},
        timeout=30,
    )

    print("Email Status:", response.status_code)
    if not response.ok:
        print(response.text, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

from datetime import datetime, timezone
import os
import requests
from requests_oauthlib import OAuth1

FIRST_POST_UTC = datetime(2026, 4, 3, 5, 0, 0, tzinfo=timezone.utc)
FIRST_DAY_NUMBER = 669

def get_day_number(now_utc: datetime) -> int:
    delta_days = (now_utc.date() - FIRST_POST_UTC.date()).days
    return FIRST_DAY_NUMBER + delta_days

def main():
    now_utc = datetime.now(timezone.utc)
    day_number = get_day_number(now_utc)
    tweet_text = f"Nope. Day {day_number}."

    auth = OAuth1(
        os.environ["X_API_KEY"],
        os.environ["X_API_SECRET"],
        os.environ["X_ACCESS_TOKEN"],
        os.environ["X_ACCESS_TOKEN_SECRET"]
    )

    response = requests.post(
        "https://api.x.com/2/tweets",
        json={"text": tweet_text},
        auth=auth,
        timeout=30
    )

    print("Status:", response.status_code)
    print("Response:", response.text)
    response.raise_for_status()

if __name__ == "__main__":
    main()
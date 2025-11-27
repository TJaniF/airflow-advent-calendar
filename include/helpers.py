import os
from datetime import datetime

FAKE_DATE = os.getenv("FAKE_DATE", None)


def get_todays_date():
    if FAKE_DATE:
        today = FAKE_DATE
    else:
        today = datetime.now().strftime("%Y-%m-%d")

    return today

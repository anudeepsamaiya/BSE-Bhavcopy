import io
import os
import requests
import zipfile

from dataclasses import dataclass
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta, FR


@dataclass
class Bhavcopy:
    TYPE_EQUITY: str = "Equity"
    DATE_FORMAT_EQUITY: str = "EQ%d%m%y_CSV"


class BhavcopyError(Exception):
    pass


def get_bhavcopy_url(bhavcopy_type: str, bhavcopy_name: str):
    bhavcopy_homepage = "https://www.bseindia.com/download/BhavCopy"
    return f"{bhavcopy_homepage}/{bhavcopy_type}/{bhavcopy_name}.ZIP"


def get_bhavcopy(bhavcopy_type: str):
    date = datetime.today()
    if date.isoweekday in (6, 7):
        date = date + relativedelta(weekday=FR(-1))
    elif not date.hour > 17:
        date = date + timedelta(-1)
    bhavcopy_name = f"{date.strftime(Bhavcopy.DATE_FORMAT_EQUITY)}"

    response = requests.get(get_bhavcopy_url(bhavcopy_type, bhavcopy_name))

    if (response.status_code // 100) in (4, 5):
        raise BhavcopyError(
            f"Unable to fetch bhavcopy. Response={response.status_code}"
        )

    bhavzip = zipfile.ZipFile(io.BytesIO(response.content))
    return bhavzip.extract(bhavcopy_name.replace("_", "."))

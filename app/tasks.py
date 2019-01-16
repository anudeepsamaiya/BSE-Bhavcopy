from .bhavcopy import get_bhavcopy, Bhavcopy
from .bseparser import populate_data_into_redis
from .celery import app


@app.task
def refresh_data():
    bhavcopy = get_bhavcopy(Bhavcopy.TYPE_EQUITY)
    populate_data_into_redis(bhavcopy)

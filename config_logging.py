import logging
import sys
from datetime import datetime
import os

import pytz

# app name
app_name = os.environ.get('app', 'quora-lite')

WS_LOG_PATH = os.path.join(os.path.curdir, "logs")  # '.\\logs'

if not os.path.exists(WS_LOG_PATH):
    os.makedirs(WS_LOG_PATH)

DATE_FORMAT = "%Y-%m-%d"
TODAY = datetime.now().strftime(DATE_FORMAT)
LOG_FILE = os.path.join(WS_LOG_PATH, f"{TODAY}_logs.log")  # '.\\2023_03_11_10_18_logs.log'

# Define time zones
utc_tz = pytz.utc
cet_tz = pytz.timezone('Europe/Berlin')
ist_tz = pytz.timezone('Asia/Kolkata')


# Custom formatter to include multiple time zones
class CustomFormatter(logging.Formatter):
    def formatTime(self, record, datefmt = None):
        utc_time = datetime.fromtimestamp(record.created, utc_tz).strftime('%Y-%m-%d %H:%M:%S')
        cet_time = datetime.fromtimestamp(record.created, cet_tz).strftime('%Y-%m-%d %H:%M:%S')
        ist_time = datetime.fromtimestamp(record.created, ist_tz).strftime('%Y-%m-%d %H:%M:%S')
        return f"[ UTC: {utc_time} | CET: {cet_time} | IST: {ist_time} ]"


# logging
log = logging.getLogger(app_name + '_logger')
log.setLevel(logging.DEBUG)
logFormatter = CustomFormatter('%(asctime)s - %(filename)s > %(funcName)s() # %(lineno)d [%(levelname)s] %(message)s')

consoleHandler = logging.StreamHandler(stream = sys.stderr)
consoleHandler.setFormatter(logFormatter)
log.addHandler(consoleHandler)

fileHandler = logging.FileHandler(LOG_FILE)  # '.\\logs/.\\2023_03_11_10_18_logs.log'
fileHandler.setFormatter(logFormatter)
log.addHandler(fileHandler)

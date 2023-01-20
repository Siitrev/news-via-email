import requests
from pprint import pprint
from datetime import datetime, timedelta
from utils.constants import (SENDER_ADDRESS,SENDER_PASSWORD,SMTP_SERVER_ADDRESS,RECIEVER_ADDRESS,PORT)
from utils.helper import send_email

today = datetime.now()
yesterday = today - timedelta(1)
topic = "warhammer"

API_KEY = "b6a87559a8a24e2a9dcf27c1c83ce34c"
url = f"https://newsapi.org/v2/everything?"\
    f"q={topic}&"\
    "language=en&"\
    "searchln=title,description&"\
    f"from={yesterday.strftime('%Y-%M-%d')}&to={today.strftime('%Y-%M-%d')}&"\
    f"sortBy=publishedAt&apiKey={API_KEY}"

# Make request
res = requests.get(url)

# Check whether error occured
res.raise_for_status()

# Read data
content = res.json()
message = """"""
for i in content["articles"][:20]:
    message += i["title"] + "\n"
    message += i["description"] +"\n"
    message += i["url"] +"\n"
    message += "\n\n"

send_email(SENDER_ADDRESS,SENDER_PASSWORD,RECIEVER_ADDRESS,SMTP_SERVER_ADDRESS,PORT,message,"NEWS")

import requests, pprint
from datetime import datetime

API_KEY = "b6a87559a8a24e2a9dcf27c1c83ce34c"
url = f"https://newsapi.org/v2/everything?q=warhammer&language=en&searchln=title,description&from="\
        f"{datetime.now().strftime('%Y-%M-%d')}&to="\
        f"{datetime.now().strftime('%Y-%M-%d')}&sortBy="\
        f"publishedAt&apiKey={API_KEY}"

# Make request
res = requests.get(url)

# Check whether error occured
res.raise_for_status()

# Read data
content = res.json()

pprint.pprint(content["articles"])
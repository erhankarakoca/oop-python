# Api Key :  749595485081424d858da6aa003c13c3
import requests
from pprint import pprint
class NewsFeed:

    def __init__(self, data):
        self.data = data

    def get(self):
        pass


url = "https://newsapi.org/v2/everything?"\
      "q=globalwarming&" \
      "from=2023-06-26&" \
      "sortBy=publishedAt&" \
      "apiKey=749595485081424d858da6aa003c13c3"

response = requests.get(url)
content = response.json()
articles = content["articles"]


# for article in articles:
#     print(article["title"], article["url"])

email_body = " "
for article in articles:
    email_body = email_body + article['title'] + "\n" +article['url'] + "\n\n"

print(email_body)
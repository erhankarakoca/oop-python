# Api Key :  749595485081424d858da6aa003c13c3
import requests
from pprint import pprint
class NewsFeed:
    """Representing multiple news titles and links as a single string
    """
    base_url = "https://newsapi.org/v2/everything?"
    api_key = "749595485081424d858da6aa003c13c3"

    def __init__(self, interest, from_date, to_date, language='en'):
        self.interest = interest
        self.from_date = from_date
        self.to_date = to_date
        self.language = language

    def get(self):
        url = self._build_url()

        articles = self._get_articles(url)

        email_body = " "
        for article in articles:
            email_body = email_body + article['title'] + "\n" + article['url'] + "\n\n"

        return email_body

    def _get_articles(self, url):
        response = requests.get(url)
        content = response.json()
        articles = content["articles"]
        return articles

    def _build_url(self):
        url = f"{self.base_url}" \
              f"qInTitle={self.interest}&" \
              f"from={self.from_date}&" \
              f"to={self.to_date}&" \
              f"language={self.language}&" \
              f"apiKey={self.api_key}"
        return url


news_feed = NewsFeed(interest="nasa", from_date="2023-07-24", to_date="2023-07-25", language="en")
print(news_feed.get())
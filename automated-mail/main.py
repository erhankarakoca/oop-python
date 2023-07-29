import yagmail
import pandas
from news import NewsFeed
df = pandas.read_excel('people.xlsx')
import datetime
import time


def send_email():
    today = datetime.datetime.now().strftime('%Y-%m-%d')
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    news_feed = NewsFeed(interest=row['interest'],
                         from_date=yesterday,
                         to_date=today)
    print(row['email'])
    email = yagmail.SMTP(user="developertools.cool@gmail.com", password="pxhlbhwbbzthodrb")
    email.send(to=row["email"],
               subject=f"Your {row['interest']} news for today! ",
               contents=f"Hi, {row['name']}\ See what's on about {row['interest']} today. \n{news_feed.get()}",
               attachments="design.txt")


while True:
    if datetime.datetime.now().hour == 17 and datetime.datetime.now().minute == 51:
        print('Executing!')

    for index, row in df.iterrows():
        send_email()

        time.sleep(60)
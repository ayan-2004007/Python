# Build a news CLI which prints 10 current news's Headline, Title, Source, Author, Published at, URL  about any sources or domain (like : Tesla, bitcoin etc)


import requests
import json
import os
from dotenv import load_dotenv

def getNews(NEWS_API,API_KEY,topic):
    try:
        res=requests.get(f"{NEWS_API}{topic}&language=en&apikey={API_KEY}")
        data=res.json()
        if res.status_code!=200:
            print(f"Internal Server Error : {data['message']}")
            return
        news=data["articles"]
        print("="*150)
        print(" "*50,"TOP 10 ONLINE NEWS")
        print("="*150)
        for i in range(10):
            print(f"{'TITLE :':<20}{news[i]['title']}")
            print(f"{'DESCRIPTION :':<20}{news[i]['description']}")
            print(f"{'AUTHOR :':<20}{news[i]['author']}")
            print(f"{'SOURCE :':<20}{news[i]['source']['name']}")
            print(f"{'URL :':<20}{news[i]['url']}")
            print("-"*150)

    except Exception as e:
        print(f"Something went wrong while fetching the data : {e}")

def main():
    load_dotenv()
    NEWS_API=os.getenv("NEWS_API")
    API_KEY=os.getenv("API_KEY")
    topic=str(input("Enter the news topic you are looking for : ")).lower().strip()
    getNews(NEWS_API,API_KEY,topic)


if __name__=="__main__":
    main()
import requests
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://newsapi.org/v2/top-headlines"
def fetch_news(source=None, keyword=None):
    params = {
        "apiKey": API_KEY,
        "country": "us",
        "pageSize": 20
    }

    if source:
        params["sources"] = source

    if keyword:
        params["q"] = keyword

    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("Error fetching news")
        return []

    data = response.json()
    articles = data.get("articles", [])

    news_list = []

    for article in articles:
        news = {
            "title": article.get("title"),
            "source": article.get("source", {}).get("name"),
            "date": article.get("publishedAt"),
            "url": article.get("url")
        }

        news_list.append(news)

    return news_list
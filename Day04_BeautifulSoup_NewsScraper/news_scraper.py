
#########################################################################################

import requests
from bs4 import BeautifulSoup

def get_news_headlines(url):
    """
    Extracts news headlines from the provided news website URL
    """
    try:
        # Fetch the HTML content
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f" Error fetching the URL: {e}")
        return []

    # Parse the HTML using BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    # Find all headline elements
    headline_elements = soup.find_all(['h2', 'h3'])

    headlines = []
    for element in headline_elements:
        headline_text = element.get_text(strip=True)
        if headline_text and len(headline_text.split()) > 3:
            headlines.append(headline_text)

    # Remove duplicates
    return list(set(headlines))


if __name__ == "__main__":
    news_url = "https://www.bbc.com/news"
    headlines = get_news_headlines(news_url)

    if headlines:
        print(f"\n Headlines from {news_url}:\n")
        for i, headline in enumerate(headlines[:15], start=1):
            print(f"{i}. {headline}")
    else:
        print(" No headlines found.")

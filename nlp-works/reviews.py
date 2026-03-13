import requests
from bs4 import BeautifulSoup

url = "https://www.amazon.in/product-reviews/B0B11LJ69K"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

reviews = soup.find_all("span", {"data-hook": "review-body"})

for i, review in enumerate(reviews[:5]):
    print(f"Review {i+1}:")
    print(review.get_text(strip=True))
    print("-"*50)
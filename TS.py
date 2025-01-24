import requests
from bs4 import BeautifulSoup

# Target website for scraping
url = "http://quotes.toscrape.com/"

try:
    # Send a GET request
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Successfully fetched the webpage!")
        
        # Parse the HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find all quote blocks
        quotes = soup.find_all("div", class_="quote")
        
        # Extract and print each quote and its author
        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()
            print(f"Quote: {text}")
            print(f"Author: {author}")
            print("-" * 40)
    else:
        print(f"Failed to fetch webpage. Status code: {response.status_code}")
except Exception as e:
    print(f"An error occurred: {e}")

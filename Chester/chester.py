import requests
from bs4 import BeautifulSoup
import psycopg2

# Database connection setup
try:
    conn = psycopg2.connect(
        dbname="investigation",
        user="postgres",
        password="Armyof_1234",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()  # Create a cursor object for executing SQL commands
    print("Database connection established successfully!")
except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")
    exit()

# List of URLs to scrape
urls = [
    "https://en.wikipedia.org/wiki/Chester_Bennington",
    "https://www.rollingstone.com/music/music-news/chester-bennington-found-dead-at-41-201017/",
    "https://www.nme.com/news/music/chester-bennington-death-linkin-park-here-are-tributes-2105673",
    "https://edition.cnn.com/2017/07/20/entertainment/chester-bennington-death-linkin-park-trnd/index.html",
    "https://www.bbc.com/news/entertainment-arts-40602472",
    "https://linkinpark.com/",
    "https://www.rollingstone.com/music/music-features/chester-bennington-linkin-park-interview-954542/",
    "https://www.theguardian.com/music/2017/jul/20/chester-bennington-death-linkin-park"
]

# Function to scrape data and insert into the database
for url in urls:
    try:
        print(f"Scraping {url}...")

        # Get page content
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract title and text
        title = soup.title.string.strip() if soup.title else "No title found"
        content = soup.get_text()

        # Save data to PostgreSQL
        cursor.execute(
    "INSERT INTO chester_info (url, title, content) VALUES (%s, %s, %s)",
    (url, title, content)
)

        print(f"Data from {url} saved to database.")
    except Exception as e:
        print(f"Error scraping {url}: {e}")

# Commit changes and close the connection
conn.commit()
cursor.close()
conn.close()
print("Scraping completed and data saved to the database!")

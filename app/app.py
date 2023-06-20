from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route('/', methods=['GET'])
def scrape_books():
    base_url = 'https://books.toscrape.com'
    url = base_url + '/catalogue/category/books_1/index.html'

    scraped_books = []

    while True:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract book information from the current page
        books = soup.select('.product_pod')
        for book in books:
            title = book.select_one('h3 a')['title']
            book_url = base_url + book.select_one('h3 a')['href']
            scraped_books.append({'title': title, 'url': book_url})
        
        # Check if there's a next page
        next_page = soup.select_one('.next a')
        if next_page:
            url = base_url + '/' + next_page['href']
        else:
            break
    
    return render_template('index.html', books=scraped_books)
    
    return jsonify(scraped_books)

if __name__ == '__main__':
    app.run()


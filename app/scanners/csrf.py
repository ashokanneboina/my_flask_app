import requests
from bs4 import BeautifulSoup

def test_csrf(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    forms = soup.find_all('form')
    
    for form in forms:
        if 'csrf' not in str(form):
            return ["Potential CSRF vulnerability: Form without CSRF token"]
    
    return ["the website is not vulunerable to csrf"]

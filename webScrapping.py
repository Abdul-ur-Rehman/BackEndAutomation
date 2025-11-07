from bs4 import BeautifulSoup
import requests

url = "https://www.udemy.com/courses/search/?src=ukw&q=appium"

data = requests.get(url)
soup = BeautifulSoup(data.content, "html.parser")

print(soup.prettify())
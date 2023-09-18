import requests
from bs4 import BeautifulSoup

url = "http://www.aozora.gr.jp/cards/000148/files/789_14547.html"
word = "猫"

# URLからHTMLを取得
response = requests.get(url)
html = response.content

# HTMLを解析
soup = BeautifulSoup(html, "html.parser")

# 単語を数える
count = str(soup).count(word)

print(f"{word}は{count}回出現しました。")
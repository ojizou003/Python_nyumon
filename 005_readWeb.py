import requests
from bs4 import BeautifulSoup

print("データをダウンロード中です...")

url="http://www.aozora.gr.jp/cards/000148/files/789_14547.html"

response = requests.get(url)
html=response.content
data=BeautifulSoup(html,"html.parser")


def wordcount(data,word):
  n = str(data).count(word)
  print(f"{word}は{n}回でてきました。\n")

while True:
  print("「吾が輩は猫である」の中で探したい言葉を入力してください。")
  print("検索を中止するときは「おわり」と入力してください。")

  word = input()
  
  if word =="おわり":
    print("ありがとうございました。またのお越しを。")
    quit()
  else:
    wordcount(data,word)

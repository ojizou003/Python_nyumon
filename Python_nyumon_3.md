# 「プログラミング超初心者が初心者になるためのPython入門 3」 たっく、ちょっぷ 著

2023/9/17~9/18

## 関数・クラス編

## whileステートメント

while 条件式 : 処理 処理後の処理

## 関数

関数の定義
def 関数名():処理

関数の呼び出し
関数名()

関数の基本は、引数を関数で処理して、戻り値を返す

## ラムダ式

関数名 ＝ lambda 引数:処理(戻り値)
double = lambda x:x*2
y = double(5)
print(y) ->10

## 関数の中の変数

## 変数のスコープ

LEGBルール ..PythonはLEGBの順番に変数を探しに行く

- ローカル ..関数の中の変数
- エンクロージング ..関数が関数を含む場合、外側の関数に含まれる変数
- グローバル ..関数の外側に書かれた変数
- ビルトイン ..Pythonがはじめから持っている__builtin__というモジュールに含まれている変数

## クラスの基本

クラスの定義
class myclass():
  def myname(self,who):  #クラス内容の記述、defでメソッドを定義
    self.name = who

person1 = myclass()  ..インスタンスの作成  (インスタンス･･･実体)

※クラスに含まれる関数は引数の扱いが通常とは異なる
  第1引数のselfはインスタンスそのものを示す
  クラスの中で定義された関数は、インスタンスに何らかの影響を目的として作られるので、インスタンス自身を示す引数を第1引数として予約してある

## 継承

継承とは、あるクラスの特徴を引き継いで別のクラスを作ること
class クラス名(親クラス名):

## ウィンドウの作成

tkinter

```Python
import tkinter

window1=tkinter.Tk()
window1.mainloop()
```

## ~~raw_~~input関数で対話式のプログラムを作る

注意）入力した値はすべて文字列として認識されてしまうので、演算する時は数値型に変更する必要がある

## Fizz buzz 問題

## 自販機問題

## Webページの読み込み

~~urllib2.request~~BeautifulSoupモジュールを使い、Webページを読み込み解析


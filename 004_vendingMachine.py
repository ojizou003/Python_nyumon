print("いらっしゃいませ。お金を入れてください。")

money = input()
money = int(money)

if money < 100:
  print("最低100円は入れてください。")
  print(money,"円お返しします。")
  quit()


while money >= 100:
    print("\n残金は",money,"円です")

    print("どの商品になさいますか？")
    print("1.お水","100円")
    print("2.ジュース","150円")
    print("3.高級玉露","180円")
    print("4.買わない")
    print("_"*50)
    print("商品番号を入力してください")
    print("_"*50)

    drink=input()

    if drink=="4":
      break
    elif drink =="1" and money >=100:
      money = money-100
      print("お水ですね。100円になります！")
    elif drink =="2" and money >=150:
      money = money-150
      print("ジュースですね。150円になります！")
    elif drink =="3" and money >=180:
      money = money-180
      print("高級玉露ですね。180円になります！")
    else:
      print("金額が足りません\n")

if money == 0:
  print("おつりはありません。ありがとうございました！")
else:
  print("\nおつりは"+str(money)+"円です。ありがとうございました！")    
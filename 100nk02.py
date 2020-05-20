#最初にUTF-8に設定しておく
#-*- coding: utf-8 -*-

#パトカーとタクシーを変数に代入する
pat = "パトカー"
tax = "タクシー"

#あらかじめ"パタトカシーー"を入れる変数を用意しておく
#文字列を入力するため""を設定しておく
moji = ""

#for文を用いて文字を先頭から交互に用意した変数に格納する
#zipを利用することで先頭から一番短い文字の長さまで順に連結してくれる
for x, y in zip(pat, tax):
	moji += x + y

#最終的にmojiに格納されているのを呼び出す
print(moji)


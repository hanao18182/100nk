#UTF-8を設定しておく
#-*- coding: utf-8 -*-

#円周率の問題の文を変数bunに入れる
bun = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

#問題の文を単語ごとに分ける
#変数stripで(","".")を使い,.を抜いて単語だけを抽出する
bun = bun.replace(",","")
buns = bun.replace(".","")

#splitで単語に1つ1つ単語に分けることができる
tan = buns.split()

#最終的に入れるリストを作成し変数pi(円周率π)に入れておく
pi = []

#for文でtanに入っている単語１つ１つの数をカウントさせる
#カウントさせた数を用意しておいたリストにどんどん入れていくようにする
for i in tan:
    a = len(i)
    pi.append(a)

#変数piに入っている結果を出力
print(pi)

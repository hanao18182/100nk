#UTF-8を設定しておく
#coding: utf-8

#入力されたbun(文章)を1文字(単語)ずつ、ずらしながらn文字分抜き出す
def n_gram (bun,n):
    return[bun[ngm:ngm + n] for ngm in range(len(bun) - n + 1)]

X = "paraparaparadise"
Y = "paragraph"

#集合を扱うための方であるset型を用いる
#set型はリスト型の様に、複数の値を格納できる型です
#printを使い出力する際はstrをつけてあげる事で出力できるようになる(strなしの場合エラー)

#まずXとYの集合をset型を使って求めsyugo_x、syugo_yに入れる
syugo_x = set(n_gram(X,2))
syugo_y = set(n_gram(Y,2))

#set型を使って求めた集合を出力する
print("Xの集合は" + str(syugo_x) + "です。")
print("Yの集合は" + str(syugo_y) + "です。")

#次にXとYの和集合を求めたset型を用いて求めwasyugoに入れる
#.unionを利用して求める(演算子「｜」でも同じことができる)
wasyugo = set.union(syugo_x,syugo_y)

#求めた和集合を出力する
print("XとYの和集合は" + str(wasyugo) + "です。")

#次にXとYの積集合を求めたset型を用いて求めsekisyugoに入れる
#演算子「＆」を利用する事で求められる
sekisyugo = syugo_x & syugo_y

#求めた積集合を出力する
print("XとYの積集合は" + str(sekisyugo) + "です。")

#次にXとYの差集合を求めたset型を用いて求めsasyugoに入れる
#differenceを利用し求められる(演算子「－」でも同様の結果が得られる)
sasyugo = set.difference(syugo_x,syugo_y)

#求めた差集合を出力する
print("XとYの差集合は" + str(sasyugo) + "です。")

#最後にset型を用いて"se"がXまたはYに含まれるか調べる
#a in b で確かめることで、aがbに含まれているとTrue・含まれていない場合Falseをかえす
print("seはXに含まれていますか？  " + str("se" in syugo_x))
print("seはYに含まれていますか？  " + str("se" in syugo_y))

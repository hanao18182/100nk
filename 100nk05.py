#UTF-8を設定しておく
#coding: utf-8

"""bigram(2文字づつ抜き出す場合)文字数10文字の場合9個出力される
   trigram(3文字づつ抜き出す場合)文字数10文字の場合8個出力される
   上記のように抜き出したい文字数(例えば10文字の時)は2文字づつだと-1の9個出力
   3文字づつだと-2の8個出力4文字づつだと-3の7個出力されると規則性が存在する。"""


#入力されたbun(文章)を1文字(単語)ずつ、ずらしながらn文字分抜き出す
#def n_gram(n-gramの関数)　(引数１、引数2)
def n_gram (bun,n):
#returnを利用して与えられた文章を1文字(単語)ずつリストにn(printする際に指定する文字分)だけ抜き出し出力させる
    return[bun[ngm:ngm + n] for ngm in range(len(bun) - n + 1)]

#bunにn-gramの問題文の文章を入れる
bun = "I am an NLPer"

#bunに入っている文章をaplit関数を使って単語ごとに分ける
tan = bun.split(" ")

#bigramを求めるので2にしてbunに入っている文字を1文字づつ抜き出しリストにて出力する
print(n_gram(bun,2))

#bigramを求めるので2にしてtan(単語にわけてある)を順番に２つづつ抽出しその結果を出力する
print(n_gram(tan,2))

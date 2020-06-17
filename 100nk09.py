#UTF-8を設定しておく
#coding: utf-8

import random

#英語の文を入力させ用意しておいたbunに格納する
#inputで相手に入力させることができる
bun = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind."

#Typoglycemia関数を作成しinputで入力されたbunの5文字以上のものをランダムに生成するものを作成する
def Typoglycemia(bun):

    #result(戻り値)のリストを用意しておく。
    result = []

    """for文を使いtanで分けられた単語1つ1つを4文字以下か5文字以上かに分け
       4文字以下の場合そのまま出力し、5文字以上の場合先頭と末尾以外の文字を
       ランダムに生成し出力させるように調べリストに追加していくプログラムを作成する！"""
	#受け取った英語の文を単語ごとに分けたもの(スペースごとに区切る)を終わるまで繰り返す
    for tan in bun.split(" "):
        #もし調べたい単語列の長さが4文字以下の場合
		#len(単語列の長さを調べる) <=(以下)
        if len(tan) <= 4:
			#result(戻り値).append(1つずつ追加していく)
			#もし条件(単語列の長さが4以下の場合)に当てはまったら単語をそのまま返し１つずつ追加していく
            result.append(tan)
			#調べたい単語列の長さが5文字以上の場合のことを指す
        else:
            #先頭と末尾の文字を残してランダムに並び替えるプログラム
			#tan[1:-1]文字の先頭と末尾以外の単語の文字をmojiに入れる
            moji = list(tan[1:-1])
			#random.shuffleを使うことで指定した部分をランダムで並び替えてくれる
            random.shuffle(moji)
			#append(1つずつ追加していく)先頭+ランダムで並び替えられたもの+末尾
            result.append(tan[0] + "".join(moji) + tan[-1])
    #returnで求めたresult(リストにしたもの)を返す。関数の外に渡す
	#"".join(result)はリストを文字列にする
    return " ".join(result)

#typ(Typoglycemia)のリストを用意しておく。最後に使う
#typ = []

#bunを受け取った後def typ(bun)が実行し、その結果をtyp格納する
typ = Typoglycemia(bun)
#全ての変更した結果(ランダム)出来たものをprintで出力する
print("変更した結果は" + typ + "です。")
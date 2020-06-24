#UTF-8を設定しておく
#coding: utf-8

#文字列(mjrt)にinputを使って英語のメッセージを格納する
mjrt = input("英語のメッセージを入力してください  ")
#入力された文字列を1文字づつに分割しlistにしcharo(char1)に入れておく
charo = list(mjrt)

#cipher関数を利用して1文字づつに分けたものを小文字かそうではないかを判別する
#もし小文字の場合(219-文字コード)の文字に置き換える
def cipher(chars):
    #最終的に関数から外に返すために用意しておく
    result=[]

    #for文を利用して1文字づつに分けたものを小文字かどうかを判断する
    for w in chars:
        #if文を利用して小文字化どうかを判断する
        #.islower()で小文字かどうかを判断する
        if w.islower():
            #もし小文字だった場合に以下の処理をする
			#219文字コードに置き換えたのち、用意しておいたresultに1文字づつ入れていく
            result.append(chr(219- ord(w)))
		#小文字ではなかった場合
        else:
			#そのまま文字を用意しておいたresultに追加していく
            result.append(w)
	#returnでcipher関数の外に返すresultに入っている物を.joinを利用してもとの通りにくっつける
    return "".join(result)

#入力されて小文字かどうかを判断し置きかえ暗号化された英語のメッセージをango(暗号)にいれる
ango = cipher(chars)

#printでangoを出力する
print("暗号化された英語のメッセージは   "+ango+"  です。")

#chart(char2)に文字列を1文字づつに分けたものを入れる
chart = list(ango)

##cipher関数を利用して1文字づつに分けたものを小文字かそうではないかを判別する
#もし小文字の場合暗号化されているので複合する
def cipher(chart):
	#求めたものを格納しておくためにresultを用意しておく
    result=[]

	#for文を利用して1文字づつに分けたものを小文字かどうかを判断する
    for w in chart:
		#小文字の場合
		#if文で.islower()を使い小文字かどうかを判断する
        if w.islower():
			#暗号化された小文字を複合化しresultに追加していく
            result.append(chr(219- ord(w)))
		#小文字以外の場合
        else:
			#小文字ではなかったのでそのままresultに1文字追加する
            result.append(w)
	#resultに入っているものを関数の外に返す.joinを使って1つにする
    return "".join(result)

#cipher関数で暗号化から複合化したものをfkgo(複合)によびだし入れる
fkgo = cipher(chart)

#printでfkgoを出力する
print("複合化された英語のメッセージは   "+fkgo+"  です。")
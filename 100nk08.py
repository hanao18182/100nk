#UTF-8を設定
#coding: utf-8

#inputを利用して外部から文字列を入力させる
#inputで受け取った文字列をmjrt(文字列)に入れる
mjrt = input("英語のメッセージを入力してください  ")
#listを利用してmjrt(文字列)を1文字ずつに分割する
#1文字ずつに分割されたものをcharsの中に入れておく
chars = list(mjrt)

#cipher関数を用意し先ほど1文字ずつにわけたcharsを条件に当てはまった場合変換するようにする
def cipher(chars):
    #判定したものを関数外に返すためにresultを用意しておく
    result=[]

    #1文字ずつ分けたものをfor文で1文字ずつ判定していく
    for w in chars:
        #if文で条件に当てはまるかelse当てはまらないかを判定する
		#w(chars)がislower(小文字)の場合(if条件に当てはまる場合)
        if w.islower():
			#条件に当てはまった場合文字をchr(219- ord(w))219-文字コードに変換する
			#appendを利用し用意しておいたresultに1つずつ追加していく
            result.append(chr(219- ord(w)))
		#else条件(英子文字)に当てはまらなかった場合
        else:
			#appendを利用し用意しておいたresultに1つずつ追加していく
            result.append(w)
	#resultの中身を"".joinでバラバラだったものを1つにつなげる
	#つながって暗号化された文字列をreturnで関数の外に返す
    return "".join(result)

#cipher関数で暗号化された文字列をango(暗号)の中に入れる
ango = cipher(chars)

#printを使って暗号化された文字列を出力する
print("暗号化された英語のメッセージは   "+ango+"  です。")

#次は暗号化された文字列を複合化し元の文字列に戻す

#まずango(暗号化)された文字列を1文字ずつ判定するために1文字ずつに区切る
#それをchartの中に入れておく
chart = list(ango)

#cipher関数で暗号化された文字を複合し複合された文字列を返す関数を作成する
#先ほど1文字ずつに区切ったchartを利用して暗号化されている文字を判定し複合する
def cipher(chart):
    #暗号化されているかされていないか判定し複合化されたものを格納するresultをあらかじめ用意しておく
    result=[]

	#for文を利用して1文字づつ分けた文字列を英子文字かそうでないかを1文字ずつ判定していく
    for w in chart:
		#if文で条件に当てはまるかelse当てはまらないかを判定する
		#w(chars)がislower(小文字)の場合(if条件に当てはまる場合)
        if w.islower():
			#条件に当てはまった場合暗号化されている文字をchr(219- ord(w))219-文字コードを利用しもとの小文字に変換する
			#appendを利用し用意しておいたresultに1つずつ追加していく
            result.append(chr(219- ord(w)))
		#else条件(英子文字)に当てはまらなかった場合
        else:
			#appendを利用し用意しておいたresultに1つずつ追加していく
            result.append(w)
	#resultの中身を"".joinでバラバラだったものを1つにつなげる
	#つながって複合化された文字列をreturnで関数の外に返す
    return "".join(result)

#cipher関数で複合化された文字列を受け取りfkgo(複合)の中に入れる
fkgo = cipher(chart)

#printを利用してfkgo複合化された文字列を出力する
print("複合化された英語のメッセージは   "+fkgo+"  です。")
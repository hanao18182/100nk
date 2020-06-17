#UTF-8を設定しておく
#coding: utf-8

#文字列(mjretu)を事前に用意しておく
#{}の中に引数が入る
mjretu = "{}時の{}は{}"

#引数を受け取るbun_string(文字列を返す)関数を活用する
#def 文字列を返す (引数１,引数2,引数3)今回受け取る文字列
#def関数名()の後の：忘れがちなので気をつける
def bun_string (x,y,z):
    return mjretu.format(x,y,z)
	#return(戻り値)を使用することで任意の値を返す
	#formatを使うことで文字列に引数の値を埋め込むことができる
	#元々用意しておいたmjretu(文字列)に埋め込みたい引数(x,y,z)を指名する

#x,y,zの値をそれぞれ入れる
#x,y,z(受け取り返す文字列)
x = 12
y = "気温"
z = 22.4


#printを使って受け取った引数x,y,zの文字列を返す
#return(戻り値)を出力してあげることで引数の埋め込まれた文字列を出力できる
print(mjretu.format(x,y,z))

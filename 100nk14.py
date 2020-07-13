#utf-8を設定しておく
#coding: utf-8

#コマンド引数を受け取るためにsysをimportしておく
import sys

#popular-names.txtの場所をfileにいれておく
file = (r"C:\\Users\\RISA\\Desktop\\ゼミ\\100ノック\\100ノック(コメントなし)\\popular-names.txt")

#入力されたコマンド引数を受け取りsysに格納
sys = sys.argv
#受け取ったコマンド引数をint型に変換しnum(数字)に入れておく
#受け取ったコマンド引数の[0]はファイルの場所の情報なので[1]を指定し入力された行数を受け取る
num = int(sys[1])

with open (file) as fileobj:
    #gyobkt（行分割）にreadで読み込んだ文章をsplitで行ごとに区切ったものを入れる
    gyobkt = fileobj.read().split("\n")
    #for文を使用して出力する行を指定する
    #[:数字]で指定した数字まで出力することができる
    #数字の部分に受け取ったコマンド引数を入れることでコマンド引数で指定していた行数を出力できる
    for gyo in gyobkt[:num]:
        #printを使用して指定の行だけを出力する
        print(gyo)

#コマンドで表すと下記の様になる
#headを利用し数字で出力したい行数を指定することで出力される

#head -n10 '/cygdrive/c/Users/RISA/Desktop/ゼミ/100ノック/100ノック(コメントな し)/popularnames.txt'
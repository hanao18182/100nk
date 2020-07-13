#utf-8を設定しておく
#coding: UTF-8

#コマンド引数を受け取るためにsysをimportして用意しておく
import sys

#popular-names.txtの場所をfileに指定しておく
file = (r"C:\\Users\\RISA\\Desktop\\ゼミ\\100ノック\\100ノック(コメントなし)\\popular-names.txt")

#入力されたコマンド引数を受け取りsysに格納
sys = sys.argv
#コマンド引数をint型に変換しnum(数字)に入れる
#受け取ったコマンド引数の[0]はファイルの場所のため[1]で指定された行数の数字を受け取る
num = int(sys[1])

#with openを使用しfile(popular-names.txt)を開く
with open (file) as fileobj:
    #gyobkt（行分割）にread()で読み込んだ文章をsplitで行ごとに分割したものを入れる
    gyobkt = fileobj.read().split("\n")
    #for文を利用して受け取った行数分処理を行う
    #[-数字:]とすることで指定された数字を末尾から順にという指定にする
    #受け取ったコマンド引数を数字に入れる事でコマンド引数分末尾の行が出力される
    for gyo in gyobkt[-num:]:
        #printを利用して末尾から指定された分だけ行を出力する
        print(gyo)

#コマンドは下記のものを利用する
#tailを利用し数字を指定することで末尾から指定した数字行出力することができる

#tail -n 5 '/cygdrive/c/Users/RISA/Desktop/ゼミ/100ノック/100ノック(コメントな し)/popular-names.txt'
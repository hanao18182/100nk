#UTF-8を設定しておく
#coding: utf-8

#popular-names.txtをfileに格納しておく
file = (r"C:\\Users\\RISA\\Desktop\\ゼミ\\100ノック\\100ノック(コメントなし)\\popular-names.txt")

#with openを利用しfile(popular-names.txt)を開く
with open(file) as fileobj:
    #readでファイル内の文章をすべて読み込みsplit("\n")で改行ごとに区切る
    #上の動作が行われたものをgyoの中にいれる
    gyo = fileobj.read().split("\n")
    #各行に分けられた(gyo)をlenを利用していくつあるかをカウントする(行数のカウント)
    #上のものをprintで出力する
    print(len(gyo))

#コマンドで表すと下記の様になります。
#$ wc -l '/cygdrive/c/Users/RISA/Desktop/ゼミ/100ノック/100ノック(コメントなし)/popular-names.txt'
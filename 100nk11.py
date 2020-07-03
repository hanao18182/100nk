#UTF-8を設定しておく
#coding: utf-8

#popular-names.txtの場所を指定してfileに格納しておく
file = (r"C:\Users\RISA\Desktop\ゼミ\100ノック\100ノック(コメントなし)\popular-names.txt")

#with openを利用してfile(popular-names.txt)を開く
with open(file) as fileobj:
    #readでfileの中身をすべて読み込みtextに入れておく
    text = fileobj.read()
    #fileの中身のタブの部分をreplaceを利用して1文字のスペースに置き換える
    #上のように行われたものをokke(置換)にいれる
    okke = text.replace("\t", " ")
    #1文字分のタブが1文字分のスペースに置換られたものをprintを使い出力する
    print(okke)


#コマンドで表すとこのようになります
#$ expand -t 1 '/cygdrive/c/Users/RISA/Desktop/ゼミ/100ノック/100ノック(コメント なし)/popular-names.txt'
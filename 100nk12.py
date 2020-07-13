#UTF-8を設定しておく
#coding: utf-8

#行でリストにする→リストの1つ目を抽出しcol1へ

#popular-names.txt,col1.txt,col2.txtの各ファイルの場所をfile,file1,file2に保存する
file = (r"C:\Users\RISA\Desktop\ゼミ\100ノック\100ノック(コメントなし)\popular-names.txt")
file1 = (r"C:\Users\RISA\Desktop\ゼミ\100ノック\100ノック(コメントなし)\col1.txt")
file2 = (r"C:\Users\RISA\Desktop\ゼミ\100ノック\100ノック(コメントなし)\col2.txt")

#1列目、2列目を入れるために用意しておく
#retu1には1列目、retu2には2列目
retu1 = []
retu2 = []

#popular-names.txtを開く
fileobj = open(file)
#for文を用いてfileの中身を取り出し下記の条件や処理を行います。
for line in fileobj:
    #line.splitで１行ずつ("\t")タブで区切る
    #retuに行で区切り単語で区切ったものを入れておく
    retu = line.split("\t")
    #retu[0]先ほど区切ったものの１列目を判断しretu1（１列目をいれるリスト）に追加する
    #appendを利用し１つずつ追加していく
    retu1.append(retu[0])
    #retu[1]先ほど区切ったものの2列目を判断しretu2（2列目をいれるリスト）に追加する
    #appendを利用し１つずつ追加していく
    retu2.append(retu[1])

#retu1とretu2の中身を実際に入っているか確認してみた
#しっかり１つずつ入っていることが確認できた
#print(retu1)
#print(retu2)

#列の1文字目は抽出できた
#だが１文字しか出力されなかったのでfor文を利用して解決しました。
#gyo1 = [row[0] for row in gyo]

#file1（col1.txt）を（"w"）書き込みモードで開く
with open(file1,"w") as fileobj:
    #先ほど１列目の文字列だけを入れたretu1を.joinを利用してつなげる
    #"\n"にすることで改行してつなげるようになる
    #writeを使ってcol.txtに書き込む
    fileobj.write("\n".join(retu1))

#file1（col1.txt）を開く
with open(file1) as fileobj:
    #先ほど書き込みで書き込んだ文章をread()を利用して読み込む
    #col1にcol.txtの内容を入れる
    col1 = fileobj.read()
    #col1に入っている１列目の情報をprintを利用して出力する
    print(col1)

#file2（col2.txt）を（"w"）書き込みモードで開く
with open(file2,"w") as fileobj:
    #先ほど2列目の文字列だけを入れたretu2を.joinを利用してつなげる
    #"\n"にすることで改行してつなげるようになる
    #writeを使ってco2.txtに書き込む
    fileobj.write("\n".join(retu2))

#file2（col2.txt）を開く
with open(file2) as fileobj:
    #先ほど書き込みで書き込んだ文章をread()を利用して読み込む
    #col2にco2.txtの内容を入れる
    col2 = fileobj.read()
    #col2に入っている2列目の情報をprintを利用して出力する
    print(col2)

#開いていたfile(popular-names.txt)を閉じる
#with openを使わない場合はcloseを書く必要がある
fileobj.close()

#コマンドで表すとこのような感じになりました
#cutで切り何列目を出力したいかを数字で指定する

#cut -f 1 '/cygdrive/c/Users/RISA/Desktop/ゼミ/100ノック/100ノック(コメントなし)/popular-names.txt' > '/cygdrive/c/Users/RISA/Desktop/ゼミ/100ノック/100ノック(コメントなし)/col1.txt'
#cut -f 2 '/cygdrive/c/Users/RISA/Desktop/ゼミ/100ノック/100ノック(コメントなし)/popular-names.txt' > '/cygdrive/c/Users/RISA/Desktop/ゼミ/100ノック/100ノック(コメントなし)/col2.txt'
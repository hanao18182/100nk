#utf-8を設定しておく
#coding: utf-8

#col.txt,col2.txtの場所をcol1,col2に教えておく
col1 = (r"C:\Users\RISA\Desktop\ゼミ\100ノック\100ノック(コメントなし)\col1.txt")
col2 = (r"C:\Users\RISA\Desktop\ゼミ\100ノック\100ノック(コメントなし)\col2.txt")

#col1.txtを開きfile1に内容を保存する
file1 = open(col1)
#colt1 = file1.read()

file2 = open(col2)
#colt2 = file2.read()

#printを利用する事で実際にcolt1,colt2の文章を出力ししっかり中身を開けているか確認できる
#print(colt1)
#print(colt2)

#col1and2.txtを開きcol12に内容を保存する
col12 = (r"C:\Users\RISA\Desktop\ゼミ\100ノック\100ノック(コメントなし)\col1and2.txt")

#col12(col1and2.txt)を"w"書き込みモードで開く、エンコードはutf-8に指定しておく
with open(col12, "w", encoding = "utf_8") as fileobj:
    #for文を利用して1列目２列目の文字列を１ずつ抽出し処理を行う
    #zipを利用することで２つのファイルを同時に使用することができる
    #1列目の入れてあるcol1と２列目の入れてあるcol2を順にみていくためにfor文を用いる
    for col1, col2 in zip(file1, file2):
        #writeを利用して()内をfileobj(col1and2.txt)に書き込む
        #col1(1列目)+タブ+col2(２列目)+改行
        #rstripは右に入っている余分な空白を削除してくれるので利用
        fileobj.write(col1.rstrip() + "\t" + col2.rstrip() + "\n")

#col12(col1and2.txt)を"r"読み込みモードで開く、エンコードはutf-8に指定しておく
with open(col12, "r", encoding = "utf_8") as f:
    #col12の内用をreadを利用して読み込みcol1and2に入れる
    col1and2 = f.read()
    #printを利用してcoland2の中身を出力する
    print(col1and2)

#開いていたfile1,file2を閉じる
file1.close()
file2.close()

#コマンドを利用するとこうなりました
#pasteを利用する事で２つのファイルを簡単にくっつけることが出来ました

#paste '/cygdrive/c/Users/RISA/Desktop/ゼミ/100ノック/100ノック(コメントなし)/col1.txt' '/cygdrive/c/Users/RISA/Desktop/ゼミ/100ノック/100ノック(コメントなし)/col2.txt' > '/cygdrive/c/Users/RISA/Desktop/ゼミ/100ノック/100ノック(コメントな し)/col1and2.txt'
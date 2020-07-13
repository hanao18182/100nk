#utf-8を設定しておく
#coding: utf-8

#popular-names.txtの場所をfileに入れておく
file = (r"C:\\Users\\RISA\\Desktop\\ゼミ\\100ノック\\100ノック(コメントなし)\\popular-names.txt")

#1列目を入れるためのretu1をリストで用意しておく
retu1 = []
#重複しておらず順番に並んだ文字列を入れるためのリストを用意しておく
onlyname = []

#先ほど場所を指定したfileを開く
fileobj = open(file)
#for文を利用して指定されたものを1つずつ処理していく
for line in fileobj:
    #lineで各行に区切ったものをsplitを利用してタブごとに更に区切る
    #用意しておいたretuにタブで区切られたものを入れていく
    retu = line.split('\t')
    #retu[0]という場所にある1列目の文字列だけをappendを利用して1つずつ
    #用意しておいたretu1に入れていく
    retu1.append(retu[0])

#setを利用することでretu1の重複した文字列を排除する
#用意しておいたonlynameに入れていく
onlyname = set(retu1)
#sortedを利用して重複した文字列を排除したものを順番に並べる(アルファベット順に)
#jyunban（順番）に入れる
jyunban = sorted(onlyname)
#printを利用して重複した文字列を排除し並び替えたものを出力する
print(jyunban)

#retu1 = ("\n".join(retu1))
#print(retu1)



#コマンドで表すと下記の様になります

#1列目の表示
#cut -f 1 popular-names.txt

#重複を省いて並び替える
#sort -f popular-names.txt > popular-names_sort.txt

#重複したものを削除する
#uniq popular-names_sort.txt popular-onlyname.txt

#合体
#cut -f 1 popular-names.txt | sort | uniq > popular-onlyname.txt
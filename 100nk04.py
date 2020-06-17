#UTF-8を設定しておく
#coding: utf-8

#元素記号の問題の文を変数bunに入れる
bun = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

#onemj(1文字)を取り出す時の数字を格納しておく
onemj = {1,5,6,7,8,9,15,16,19}

#bunに入っている文章をスペースごとに区切りtanに入れる
tan = bun.split(" ")

#元素記号(Element symbol)のリストを用意する
el = {}

#for文で1文字取り出す2文字取り出すかを確かめる
#enumerate関数を利用する事でインデックスを最初から1つづつみるようにできる
#分けた単語１つ１つをonemjの数字に該当するかif文を用いて確かめる
for i,mj in enumerate(tan):
#もしリスト内のiがonemjに該当する場合は1文字をel(元素記号のリスト)に入れる
    if i + 1 in onemj:
        el[i + 1] = mj[0]
#もしリスト内のiがonemjに該当しない場合は2文字をel(元素記号のリスト)に入れる
    else:
        el[i + 1] = mj[:2]


#変数gen(元素記号)に入っている物を出力する
print(el)

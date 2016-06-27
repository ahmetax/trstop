# -*- coding: utf-8 -*-
"""
Program: Ahmet Aksoy
Tarih: 27.06.2016
Sürüm : Python 3.5.1
Türkçede kullanılan 'stop words', yani dolgu sözcükler için seçilenlerin
kullanım frekansları en yüksek ilk 10 bin sözcük arasında olup olmadığı
aşağıdaki kodlarla kontrol ediliyor.
zxtest sözcüğü özellikle kontrol amacıyla eklenmiştir.
"""

onbinlik = {}
def onbin_oku():
    dict_basla = False
    with open("/home/ax/PycharmProjects/trdp/dosyalar/derlemtr2016-10000.txt", "r",encoding="utf-8") as f:
        for line in f:
            l=line.split()
            if len(l)<=1:continue
            if l[0][0] not in ['0','1']: continue
            #print (l[1], l[0])
            onbinlik[l[1].strip()] = int(l[0].strip())

onbin_oku()

fstop = open("/home/ax/PycharmProjects/trdp/dosyalar/turkce-stop-words",encoding="utf-8")
for sat in fstop:
    stop = sat.strip()
    if stop in onbinlik.keys():
        #print("{} listede var".format(stop))
        pass
    else:
        print("{} listede yok".format(stop))

fstop.close()

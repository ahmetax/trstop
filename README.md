# trstop
Turkish Stop Words  Türkçe Dolgu Sözcükleri
In this repository I put Turkish stop words that is contained in the first 10 thousand words with the highest frequency.
In order to test the new candidate words in future, I add a small python script, and a 10 thousand item word list with highest frequency.

[sgsinclair/trombone](https://github.com/sgsinclair/trombone/blob/master/src/main/resources/org/voyanttools/trombone/keywords/stop.tr.turkish-lucene.txt) repository includes some of the Turkish stop words. However, some stop words in that list do not belong to the ten thousand highest frequency words.

## In order to use the module:

import trstop

trstop.is_stop_word(parameter)

## Contributors:

- Ahmet Aksoy
- Toprak Öztürk

Bu depoya en sık kullanılan 10 bin Türkçe sözcük listesinde yer alan dolgu sözcüklerini ekledim.
Dolgu sözcükleri (stop words), sık kullanılan, ama iptal edildiklerinde ayrıldıkları cümlenin anlamında önemli değişiklikler oluşturmayan sözcüklerdir.

"Stop words" terimine karşılık "dolgu sözcükleri" terimini kullandım. Daha iyi bir seçenek varsa, değiştirmeye hazırım.
Depoya eklediğim "turkce-stop-words-dict.py" betiğini, ileride listeye yeni sözcükler eklemek istediğimizde kullanım sıklığını denetlemek amacıyla kullanabiliriz.

https://github.com/sgsinclair/trombone/blob/master/src/main/resources/org/voyanttools/trombone/keywords/stop.tr.turkish-lucene.txt  adresinde de bazı dolgu sözcükleri listelenmiş. Ancak buradaki bazı sözcükler ilk onbine girecek kadar yoğun frekansa sahip değil.

## Modülü kullanmak için:

import trstop

trstop.is_stop_word(parametre)

## Projeye katkıda bulunanlar:

- Ahmet Aksoy
- Toprak Öztürk

Son güncelleme: 07.10.2016



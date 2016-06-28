# trstop
Turkish Stop Words  Türkçe Dolgu Sözcükleri
In this repository I put Turkish stop words that is contained in the first 10 thousand words with the highest frequency.
In order to test the new candidate words in future, I add a small python script, and a 10 thousand item word list with highest frequency.
In order to use the module:
import trstop
trstop.is_stop_word(parameter)

Contributors:
Ahmet Aksoy
Toprak Öztürk

Bu depoya en sık kullanılan 10 bin Türkçe sözcük listesinde yer alan dolgu sözcüklerini ekledim.
Dolgu sözcükleri (stop words), sık kullanılan, ama iptal edildiklerinde ayrıldıkları cümlenin anlamında önemli değişiklikler oluşturmayan sözcüklerdir.

"Stop words" terimine karşılık "dolgu sözcükleri" terimini kullandım. Daha iyi bir seçenek varsa, değiştirmeye hazırım.
Depoya eklediğim "turkce-stop-words-dict.py" betiğini, ileride listeye yeni sözcükler eklemek istediğimizde kullanım sıklığını denetlemek amacıyla kullanabiliriz.

Modülü kullanmak için:

import trstop
trstop.is_stop_word(parametre)

Projeye katkıda bulunanlar:
Ahmet Aksoy
Toprak Öztürk

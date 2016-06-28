# -*- coding: utf-8 -*-
"""
Program: Ahmet Aksoy
Tarih: 27.06.2016
Sürüm : Python 3.5.1
Düzenleme: Toprak Öztürk
Türkçede kullanılan 'stop words', yani dolgu sözcükler için seçilenlerin
kullanım frekansları en yüksek ilk 10 bin sözcük arasında olup olmadığı
aşağıdaki kodlarla kontrol ediliyor.
zxtest sözcüğü özellikle kontrol amacıyla eklenmiştir.
"""

dictionary = {}


# lisans bilgisini de barindaridan sozluk dosyasini ac
with open("dosyalar/derlemtr2016-10000.txt", 'r', encoding = 'utf-8') as fdict:
	for line in fdict:
		# lisansa ait olan satirlari yoksay ve bos satirlari atla
		if (line[0] not in ['0', '1']):
			continue

		freq, word = line.strip().split()
		dictionary[word] = int(freq)


def is_stop_word(word):
	""" 
	parametre olarak verilen sozcugun sozlukte olup olmadigini kontrol eder.
	checks if word is in the dictionary, returns true if so.

	word: str
	return: bool
	"""
	return word in dictionary.keys()


def get_word_freq(word):
	"""
	parametre olarak verilen sozcugun frekansini geri dondurur. 
	sozcuk sozlukte yoksa 0 dondudur.
	returns usage frequency of word. returns 0 if word is not in the dict.

	word: str
	return: int
	"""
	if is_stop_word(word):
		return dictionary[word]
	else:
		return 0

if __name__ == '__main__':
	ftest = open("dosyalar/turkce-stop-words",encoding="utf-8")

	for word in ftest:
		word = word.strip()

		if not word in dictionary.keys():
			print('{} sozlukte yok'.format(word))
		is_stop_word
	ftest.close()

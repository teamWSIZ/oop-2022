# detekcja kodowania

import chardet

# s = 'spółkaćą'
# s = 'geschützte Leerzeichen'
s = 'ドイツ語とアルバニア語は 8859-1 を使うこともできるが、'
bytez = s.encode('ISO-2022-JP')

en = chardet.detect(bytez)
print(en)

ss = bytez.decode(en['encoding'])
print(ss)
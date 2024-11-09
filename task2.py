# TODO Найдите количество книг, которое можно разместить на дискете
memmory = 1.44 #МБ
Pages = 100 # Кол-во страниц
Line = 50 #Кол-во строк
Symbols = 25 #Кол-во символов в строке
Symb_1 = 4 #байт
memmory_byte = memmory*1024*1024
text = Pages*Line*Symbols
mass_text = text*Symb_1
N_books = round(memmory_byte/mass_text)
print("Количество книг, помещающихся на дискету:", N_books)

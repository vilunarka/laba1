# TODO Найдите количество книг, которое можно разместить на дискете
a = 4 * 25 * 50 * 100
k = int(( 1.44 * 1024 * 1024 ) // a)
print("Количество книг, помещающихся на дискету:",k)

# TODO Найдите количество книг, которое можно разместить на дискете
memory = 4 * 25 * 50 * 100
books = int((1.44 * 1024 * 1024) // memory)
print("Количество книг, помещающихся на дискету:", books)

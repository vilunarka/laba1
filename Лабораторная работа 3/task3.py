# TODO  Напишите функцию count_letters

def count_letters(a):
    c = ""
    simb = []
    frecuency = []

#Откидывание из исходного текста все символов, кроме букв
#Замена заглавных букв на строчные, метод lower не работал в функции
    for i in a:
        if (ord(i) >= ord("А")) and (ord(i) <= ord("я")):
            if ord(i) <= ord("Я"):
                c += chr(ord(i) + 32)
            else:
                c += i

#Составление списков символов и их количеств в тексте
    for i in range (0, 32):
        simb.append(chr(i+1072))
        frecuency.append(c.count(chr(i+1072)))

#Подсчет частоты
    for i in range(len(frecuency)):
        frecuency[i] = frecuency[i]/(len(c))
        frecuency[i] = round(frecuency[i], 2)

#Объединение двух массивов в один для удобного хранения данных
    for i in range(32):
        simb[i] = ([simb[i], frecuency[i]])
    return [simb]

# TODO Напишите функцию calculate_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""


# TODO Распечатайте в столбик букву и её частоту в тексте

a = count_letters(main_str)
a = a[0]    #Сброс дополнительного измерения массива, образовавшегося после работы функции
for i in a:
    print(i[0], end = ": ")
    print(i[1])
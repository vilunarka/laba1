def count_letters(text1):
    text1 = text1.lower()
    remade_str = ''.join(c for c in text1 if c.isalpha())
    letters = {}
    for index in range(32):
        letters[chr(index + ord('а'))] = remade_str.count(chr(index + ord('а')))
    return letters

def calculate_frequency(symbols):
    letters_frequency = {}
    total = 0
    for index in range(32):
        total += symbols[chr(index + ord('а'))]
    for index in range(32):
        frequency = symbols[chr(index + ord('а'))] / total
        letters_frequency[chr(index + ord('а'))] = frequency
    return letters_frequency

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
letters_main = count_letters(main_str)
dict = calculate_frequency(letters_main)
for index in range(32):
    print(chr(index + ord('а')), ':', round(dict[chr(index + ord('а'))], 2))

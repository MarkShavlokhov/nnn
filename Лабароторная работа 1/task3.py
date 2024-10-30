def count_letters(text):
    # Приводим текст к нижнему регистру и инициализируем словарь для подсчета
    text = text.lower()
    letter_counts = {}

    # Подсчитываем количество каждой буквы
    for char in text:
        if char.isalpha():  # Проверяем, является ли символ буквой
            letter_counts[char] = letter_counts.get(char, 0) + 1

    return letter_counts


def calculate_frequency(letter_counts):
    # Находим общее количество всех букв
    total_letters = sum(letter_counts.values())
    letter_frequencies = {}

    # Вычисляем частоту для каждой буквы
    for letter, count in letter_counts.items():
        letter_frequencies[letter] = round(count / total_letters, 2)

    return letter_frequencies


# Текст для анализа
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

# Подсчитываем количество каждой буквы
letter_counts = count_letters(main_str)

# Вычисляем частоту каждой буквы
letter_frequencies = calculate_frequency(letter_counts)

# Печатаем частоты букв в порядке их первого появления
# Для этого используем список для хранения порядка букв
order_of_appearance = []
seen_letters = set()

for char in main_str.lower():
    if char.isalpha() and char not in seen_letters:
        seen_letters.add(char)
        order_of_appearance.append(char)

# Выводим частоты в порядке их появления
for letter in order_of_appearance:
    frequency = letter_frequencies[letter]
    print(f"{letter}: {frequency:.2f}")

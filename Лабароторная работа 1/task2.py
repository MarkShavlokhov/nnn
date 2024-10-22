# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, delimiter=','):
    # Разделяем строки на списки участников
    participants1 = set(group1.split(delimiter))
    participants2 = set(group2.split(delimiter))

    # Находим пересечение двух множеств участников
    common_participants = participants1.intersection(participants2)

    # Сортируем и возвращаем список общих участников
    return sorted(common_participants)


# Пример использования с разделителем '|'
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
print(find_common_participants(participants_first_group, participants_second_group, delimiter='|'))

# TODO Провеьте работу функции с разделителем отличным от запятой

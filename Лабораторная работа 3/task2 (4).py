# TODO Напишите функцию find_common_participants

def find_common_participants(group1, group2, separator=','):
    participants_first = set(group1.split(separator))
    participants_second = set(group2.split(separator))

    common_participants = participants_first.intersection(participants_second)

    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print(f"Общие участники: {common_participants}")

# TODO Провеьте работу функции с разделителем отличным от запятой

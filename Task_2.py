def find_common_participants(group1, group2, separator="|"):
    # Разбиваем строки на списки участников, используя разделитель
    participants_group1 = set(group1.split(separator))
    participants_group2 = set(group2.split(separator))

    # Находим пересечение двух множеств
    common_participants = participants_group1.intersection(participants_group2)

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)


# Пример использования:
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common_participants = find_common_participants(participants_first_group, participants_second_group)
print(common_participants)
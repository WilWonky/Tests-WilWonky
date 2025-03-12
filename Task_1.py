def find_item_index(items, item_to_find):
    """Функция для поиска индекса товара в списке."""
    try:
        return items.index(item_to_find)  # Возвращаем индекс первого вхождения
    except ValueError:
        return None  # Если товара нет в списке, возвращаем None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_item_index(items_list, find_item)  # Вызов функции
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
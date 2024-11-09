numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
skip_1 = numbers[5:]  # всё кроме четвертого элемента
skip_2 = numbers[:4]  # всё кроме четвертого элемента
# TODO заменить значение пропущенного элемента средним арифметическим
summ_of1 = sum(skip_1) # сумма первых 4 чисел
summ_of2 = sum(skip_2) # сумма вторых 15 чисел
Summ_numbers = summ_of1+summ_of2 # сумма 19 чисел без None
len_1 = len(numbers)  # TODO количество цифр
average = round(Summ_numbers/len_1, 2) # среднее всез чисел
numbers[4] = average
print("Измененный список:", numbers)

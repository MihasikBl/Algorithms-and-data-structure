# Получает отсортированный массив и значение.
# Если значение присутствует в массиве, то функция возвращает его позицию.

# Функция создания списка
def create_list(n):
    list_x = []
    for i in range(n):
        list_x.append(int(input()))
    return list_x


# Функция бинарного поиска
def binary_search(x_list, necessary_item):
    low_index = 0
    high_index = len(x_list)-1

    while low_index <= high_index:
        middle_index = (low_index + high_index)
        suggest_item = x_list[middle_index]
        if suggest_item == necessary_item:
            return print(f"Число {necessary_item} имеет {middle_index} индекс в списке")
        if suggest_item > necessary_item:
            high_index = middle_index - 1
        else:
            low_index = middle_index + 1
    return None


x = int(input("Введите число элементов в списке = "))
nec_item = int(input("Какое число нужно найти: "))
list1 = create_list(x)
binary_search(list1, nec_item)

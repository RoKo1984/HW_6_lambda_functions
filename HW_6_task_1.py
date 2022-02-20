# Вам дан код сортировки пузырьком, однако он работает неверно, там допущена ошибка.
# Используя дебагер, найдите и исправьте ошибку. Опишите в комментарии к коду, в чем была ошибка.

# Исходный код:

# def buble_sort(l): # не верное название списка
#     t = l.copy()
#     for n in range(0, len(t)):
#         for i in range(len(t) - n):
#             if t[i] > t[n]:
#                 t[i], t[n] = t[n], t[i]
#     return t
#
# nums = [4, 1, 6, 3, 2, 7, 8]
# sorted = buble_sort(nums)
# print(sorted)


# Решение

def buble_sort(l):
    t = l.copy()
    for n in range(len(t)):  # Запись (0, len(t)) избыточна
        for i in range(len(t)): # убираем "-n"
            if t[i] > t[n]:
                t[i], t[n] = t[n], t[i]
    return t
# nums = [4, 1, 6, 3, 2, 7, 8] # заменил исходный список на рандомный для большей вариативности
import random
nums = [random.randint(0, 50) for i in range(20)]
print(f'исходный список: {nums}')
sorted = buble_sort(nums)
print(f'отсортированный список: {sorted}')


# Решение с оптимизацией (более наглядный вариан и оптимизированный по времени код)

# def buble_sort(nums):
#     t = nums.copy()
#     for n in range(len(t)):
#         for i in range(len(t) - n - 1):  # -n уменьшает количество проходов по списку в итерации;
#                                          # -1 - не берет последний элемент списка, что позволяет избежать ошибки
#                                          # при сравнении последнеднего элемента
#             if t[i] > t[i+1]:  # выполняется сравнение соседних элементов в списке, а не 'i' и 'n'
#                 t[i], t[i+1] = t[i+1], t[i]
#     return t
# import random
# nums = [random.randint(0, 50) for i in range(20)]
# print(f'исходный список: {nums}')
# sorted = buble_sort(nums)
# print(f'отсортированный список: {sorted}')


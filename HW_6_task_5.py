# Используя filter() оставьте только книги, количество которых больше 5ти

orders_old = [
[34587, 'Learning Python, Mark Lutz', 4, 40.95],
[98762, 'Programming Python, Mark Lutz', 5, 56.80],
[77226, 'Head First Python, Paul Barry', 3, 32.95],
[88112, 'Einfuhrung in Python3, Bernd Klein', 3, 24.99]
]

orders_new = [
[24387, ' на русском', 2, 4.59],
[18762, 'The C Programming Language (2nd Edition)', 12, 78.80],
[87236, 'C Programming Absolute Beginner\'s Guide', 1, 23.55],
[58132, 'Effective Modern C++: 42 Specific Ways to Improve Your Use of C++11 and C++14', 9, 42.89]
]

orders_sum = orders_old + orders_new

print(*orders_sum, sep='\n')
print('***************************************************************************')

# sorted_orders_sum = sorted(orders_sum, key=lambda x: float(x[3]))
# print(*sorted_orders_sum, sep='\n')
# print('***************************************************************************')

orders_filter = list(filter(lambda x: x[2] >= 5, orders_sum))
print(*orders_filter, sep='\n')
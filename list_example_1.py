my_list1 = list(range(1, 6))
my_list2 = list(range(6, 11))

my_list3 = my_list2 + my_list1

my_list3 *= 2

my_list3.append(-222)

my_list3 = sorted(my_list3)

my_list3.pop(2)
my_list3.pop(1)

print(my_list3)
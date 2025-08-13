my_2d_list = [
    [1, 3, 5, 7],
    [2, 3, 8, 0],
    [9, 11, 13, 15],
    [17, 19, 21, 23],
    [27, 29, 61, 33]
]

my_2d_list.append([9, 3, 4, 6, 10])

my_2d_list[2] = [12, 95, 32, 12]

my_2d_list.insert(1, [20, 69, 90, 10])

my_2d_list[2][1] = 22

print([[my_2d_list[2][1], my_2d_list[2][2]],
      [my_2d_list[3][1], my_2d_list[3][2]]])

#print(my_2d_list)
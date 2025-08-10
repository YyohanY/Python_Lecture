# [Lambda 개념]
# 일반적인 함수 정의
def add(x, y):
    return x + y

# Lambda 함수로 동일한 기능
add_lambda = lambda x, y: x + y

print(add_lambda(3, 5))  # 8


# [Lambda 응용 1 : 짝수 필터링 (filter())]
numbers = [1, 2, 3, 4, 5, 6]

# 람다 함수와 filter() 함수 사용
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # [2, 4, 6]


# [Lambda 응용 2 : 항 제곱 연산 (map())]
numbers = [1, 2, 3, 4, 5]

# 람다 함수와 map() 함수 사용
squared_numbers = list(map(lambda x: x ** 2, numbers))

print(squared_numbers)  # [1, 4, 9, 16, 25]


# [Lambda 응용 3 : 기준 정렬 (sorted()) ]
students = [('Alice', 25), ('Bob', 20), ('Charlie', 23)]

# 나이를 기준으로 정렬
students_sorted = sorted(students, key=lambda x: x[1])

print(students_sorted)  # [('Bob', 20), ('Charlie', 23), ('Alice', 25)]
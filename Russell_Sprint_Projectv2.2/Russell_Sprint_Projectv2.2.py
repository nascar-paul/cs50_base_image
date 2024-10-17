my_numbers = [5, 10, 15, 20, 25]
print (my_numbers[2])

my_strings = ["apple", "banana", "cherry"]
print (my_strings[-1])

mixed_list = [1, "two", 3.0, [4, 0]]
print (mixed_list[1])

my_numbers.append(30)
print (my_numbers)

data_points = []
data_points.append ((1,2))
data_points.append ((3,4))
data_points.append ((5,6))

graph_settings = ("Line Graph", "red", 2)

for number in my_numbers:
    print (number)

for index, value in enumerate(my_strings):
    print(f"Index {index} : {value}")
def int_in_list(list):
    return all(isinstance(x, int) for x in list)

my_list = [1, 2, 3, "string", 5]
result = int_in_list(my_list)
print(result)

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_list = [el for el in src if src.count(el) == 1]
print(f"src\n{src}\nresult\n{unique_list}")

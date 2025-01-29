my_str = input("Вкажіть щось")
my_str = list(my_str)

new_str = []

for i in my_str:
    if not i.isdigit():
        new_str.append(i)

print(new_str)
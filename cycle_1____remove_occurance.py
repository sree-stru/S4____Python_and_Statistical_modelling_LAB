numbers = list(map(int, input("Enter the number list: ").split()))
u_list = []

for i in numbers:
    if i not in u_list:
        u_list.append(i)

print("Unique list:", u_list)

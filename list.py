# Assigning elements to different lists

list = []

for i in range(0,11,2):
    list.append(i)

print(list)

list2 = ['Facebook','Amazon','Netflix','Google']
list2.append(list)
print(list2)

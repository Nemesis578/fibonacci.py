# Accessing elements from a tuple

tup = ('physics', 'chemistry', 'mathematics', 'biology');

for i in tup:
    print(i)

print(tup[2])

# Deleting different dictionary elements

dict = {
    "Name": "Lin Dan",
    "Nationality" : "Chinese",
    "Date of Birth": "14 October, 1983",
    "Age":36, 
    "Sports": "Badminton",
    "Sponsorship": "Yonex",
    "Handedness" : "Left",
    "Coach": "Xia Xianze",
}

dict.pop("Coach")

print(dict)

# Assigning elements to different lists

list = []

for i in range(0,11,2):
    list.append(i)

print(list)

list2 = ['Facebook','Amazon','Netflix','Google']
list2.append(list)
print(list2)

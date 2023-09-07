# merge and sort two array


# Merge and sort two arrays

f_list = []
s_list = []
num1 = int(input("Enter no.of first list:"))
for i in range(1, num1 + 1):
    a = int(input("Enter element:"))
    f_list.append(a)

num2 = int(input("Enter no.of second list:"))
for i in range(1, num2 + 1):
    b = int(input("Enter element:"))
    s_list.append(b)

t_list = f_list + s_list
t_list.sort()
print("Sorted list is:", t_list)
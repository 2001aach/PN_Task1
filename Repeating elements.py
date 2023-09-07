# Find the first repeating element in an array of integers



arr = [1,3,4,4,5,3,4,6]
rpt_ele = -1

for element in arr:
    c = arr.count(element)
    if c > 1:
        rpt_ele = element
        break;

if rpt_ele == -1:
    print("There are no repeating elements in array")
else:
    print("The first repeating element is", rpt_ele)
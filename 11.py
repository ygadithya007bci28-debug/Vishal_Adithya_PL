input_str =[1,5,7,9,11,17,19,27,45,50]
N=input_str
L1 = []
L2 = []
for num in N:
    if num % 2 == 0 and num % 3 != 0:
        L1.append(num)
    if num % 9 == 0:
        L2.append(num)
print("MyList1 (Divisible by 2, not 3):", *L1)
print("MyList2 (Multiples of 9):", *L2)


numbers = [1, 5, 7, 9, 11, 17, 19, 27, 45, 50]
MyList1 = [x for x in numbers if x % 2 == 0 and x % 3 != 0]
MyList2 = [x for x in numbers if x % 9 == 0]
print(*(MyList1 + MyList2))

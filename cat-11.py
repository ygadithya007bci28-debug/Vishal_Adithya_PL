L=[14,21,5,28,7,50,42,14,7,35,21,4,10,35]
S=set(L)
S7={num for num in range(1, 51) if num % 7 == 0}
IS=S.intersection(S7)
RL= sorted(list(IS))
print(f"Initial list: {L}")
print(f"Set from list (duplicates removed): {S}")
print(f"Set of numbers 1 to 50 divisible by 7: {S7}")
print(f"Intersection of both sets: {IS}")
print(f"Result as a sorted list: {RL}")

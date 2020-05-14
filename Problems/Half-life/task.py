atoms_n = int(input())
quantity_r = int(input())
days = 0
while atoms_n >= quantity_r:
    atoms_n /= 2
    days += 12
print(days)
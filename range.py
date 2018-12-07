numbers = list(range(2000, 3201))
 range.py
for x in numbers:
    if x % 7 == 0 and x % 5 != 0:

        print(str(x) + ",", end='')

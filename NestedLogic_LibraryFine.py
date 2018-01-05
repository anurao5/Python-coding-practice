#If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0
#If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, .
#If the book is returned after the expected return month but still within the same calendar year as the expected return date, the .
#If the book is returned after the calendar year in which it was expected, there is a fixed fine of .

d1, m1, y1 = map(int, input().split(' '))
d2, m2, y2 = map(int, input().split(' '))

fine = 0

if y1 > y2:
    fine = 10000
elif y1 < y2:
    fine = 0
else:
    if m1 > m2:
        fine = 500 * (m1 - m2)
    elif m1 < m2:
        fine = 0
    else:
        if d1 > d2:
            fine = 15 * abs(d1 - d2)
        elif d1 <= d2:
            fine = 0

print(fine)

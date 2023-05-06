'''
Write a Python program to count the number of even and odd numbers from
a series of numbers (1, 2, 3, 4, 5, 6, 7, 8, 9)?
'''

even = 0
odd = 0
for i in range (1,10):
    if i % 2 == 0:
        even +=1
    else:
        odd +=1

print("Numbers of even number : ",even)
print("Numbers of odd number :",odd)

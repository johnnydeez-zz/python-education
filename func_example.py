

'''
WHY ARE FUNCTIONS IMPORTANT?

Sure, you could just do the same thing over and over
'''

print("\n")
result = 2 + 7 
print("2 + 7 equals "  + str(result) + ".")

print("\n")
result = 3 + 2 
print("3 + 2 equals " + str(result) + ".")


print("\n")
result = 1 + 9 
print("1 + 9 equals " + str(result) + ".")


print("\n")
result = 0 + 4 
print("0 + 4 equals " + str(result) + ".")



'''
This, however is much simpler. Now we can just call our function
as many times as we want.
'''

print("------------------------------")

def what_equals_what(x, y):
    print("\n")
    result = x + y 
    print(str(x) + " + " + str(y) + " equals " + str(result) + ".")

what_equals_what(9, 9)
what_equals_what(1, 1)
what_equals_what(2, 4)


'''
Better yet, we can loop our function so we only need a few lines
to repeat our operation.
'''
print("------------------------------")

numbers = [
    [1,1],
    [2,2],
    [3,3]
]

for group in numbers:
    what_equals_what(group[0], group[1])




















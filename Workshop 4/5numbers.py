'''ask user for 5 numbers shows first last smallest biggest a
and the average of the numberts
'''
numbers=[]
for n in range(5):
    number=int(input("Number: "))
    numbers.append(number)
print("the first number is", numbers[0])
print("the last number is", numbers[-1])
print("the smallest number is", min(numbers))
print("the largest number is", max(numbers))
print("the average of the numbers is", sum(numbers)/len(numbers))
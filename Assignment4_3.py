#write a python program to square the elements of a list using map() function

def calculate_square(n):
    return n * n
numbers = [1, 4, 6, 7, 9, 5]
print("original list:",numbers)
result = map(calculate_square, numbers)

print("square of updated list:",(list(result)))
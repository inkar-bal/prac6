numbers = [3, 1, 4, 1, 5]

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))
print("Sorted:", sorted(numbers))

# map()
numbers_str = list(map(str, numbers))
print("Numbers as strings:", numbers_str)

# filter()
print("Numbers > 3:", list(filter(lambda x: x > 3, numbers)))

# reduce()
print("Sum using reduce:", reduce(lambda x, y: x + y, numbers))
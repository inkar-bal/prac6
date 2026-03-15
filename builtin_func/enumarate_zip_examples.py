names = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 78]

# enumerate()
print("Using enumerate:")
for i, name in enumerate(names):
    print(i, name)

# zip()
print("\nUsing zip:")
for name, score in zip(names, scores):
    print(name, score)

# sorted()
print("\nNames sorted by scores:")
for name, score in sorted(zip(names, scores), key=lambda x: x[1], reverse=True):
    print(name, score)

scores_str = list(map(str, scores))
print("\nScores converted to strings:", scores_str)
print("Type of scores_str:", type(scores_str))

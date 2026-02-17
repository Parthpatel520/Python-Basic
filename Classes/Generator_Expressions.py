data = 'parth'
print(list(data[i] for i in range(len(data)-1, -1, -2))) #range(start, stop, step)

print(f"sum of squares: {sum(i*i for i in range(10)) }")              


x = [10, 20, 30]
y = [10, 20, 30]
z = sum(x*y for x,y in zip(x, y)) 
print(z)


page = [
    "hello world", 
    "hello python"
    ]

unique_words = set(word for line in page  for word in line.split())
print(unique_words)



import math

a = {"apple": 1, "banana": 2, "cherry": 3, "date": 4, "elderberry": 5}
for i, j in a.items():
    print(f"{j} : {i}")
    
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)
    
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)
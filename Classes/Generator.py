for char in reversed('golf'):
    print(char)

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        
# "yield" not allowed outside of a function or lambdaPylance
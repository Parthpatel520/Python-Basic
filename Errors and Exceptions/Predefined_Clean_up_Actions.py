# file do not close automatically, we need to close it manually
with open("example.txt", "w") as f:
    content = f.read()
    print(content)

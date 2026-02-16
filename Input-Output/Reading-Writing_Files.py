f = open("example.txt", "w")
f.write("Hello, World!\n")

f = open("example.txt", "r") 
content = f.read()
print(content)

# with file atomatically closes hear
with open("example.txt", "a") as a: # 'a' stands for append mode, which allows you to add content to the end of the file without overwriting it.
    a.write("This is a new line.\n")
    
with open("example.txt", "r") as r:
    content = r.read() # Reads the entire file, which is "Hello, World!\nThis is a new line.\n"
    # content = r.readline(1) # Reads 1 byte, which is 'H'
    # content = r.readline() # Reads the first line, which is "Hello, World!\n"
    # content = r.readlines() # Reads the file into a list of lines: ["Hello, World!\n", "This is a new line.\n"]
    print(content)  
    
    
f = open("example.txt", "a")
f.write("Appending another line.\n")
f.close()

f = open("example.txt", "r")
f.seek(7)
print("Content starting from position 7:", f.read()) 


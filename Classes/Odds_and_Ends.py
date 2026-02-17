from dataclasses import dataclass

@dataclass
class student:
    """A class to represent a student."""
    name: str
    age: int
    grade: str
    
s1 = student("parth", 20, "A")
print(s1)

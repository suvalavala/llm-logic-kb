from pylog import *

# Declare facts
parent = Predicate(2)
male = Predicate(1)
female = Predicate(1)

parent("homer", "bart")
parent("homer", "lisa")
parent("marge", "bart")
parent("marge", "lisa")
parent("abraham", "homer")
parent("mona", "homer")
male("homer")
male("bart")
female("lisa")
female("marge")

# Rule
def grandparent(x, y):
    return exists(z, parent(x, z) & parent(z, y))

# Run sample query
print("Grandparents of Bart:")
for x in grandparent(var('X'), "bart"):
    print(x["X"])


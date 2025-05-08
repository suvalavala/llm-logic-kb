# symbol_llm_runner.py

from pylog import *

# Load your symbolic KB here (same as test_pylog.py)
# Example reasoning rule (mimicking Symbol-LLM interaction):
def query_grandparent(grandchild):
    parent = Predicate(2)
    def grandparent(x, y):
        return exists(z, parent(x, z) & parent(z, y))
    return [result["X"] for result in grandparent(var("X"), grandchild)]

if __name__ == "__main__":
    print("Testing symbolic reasoning over KB...")
    print("Grandparents of Bart:", query_grandparent("bart"))

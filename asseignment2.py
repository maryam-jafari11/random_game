import random
n = int(input("enter num: "))
def random_list_unique(n):
    result = set()
    while len(result) < n:
        result.add(random.randint(1, 100))
    return list(result)

print(random_list_unique(n))
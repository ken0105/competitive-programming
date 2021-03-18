child = []
def main():
    n = int(input())
    global child
    child = [[] for i in range(n + 1)]
    for i in range(2,2 + n - 1):
        parent = int(input())
        child[parent].append(i)
    salary = dfs(1)
    print(salary)

def dfs(id):
    subordinate = child[id]
    if len(subordinate) == 0:
        return 1

    salaries = []
    for mem in subordinate:
        salaries.append(dfs(mem))

    return max(salaries) + min(salaries) + 1





if __name__ == '__main__':
    main()

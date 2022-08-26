if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n==len(list(arr)):
        a = set([i for i in arr])
        b = max(a)
        a.remove(b)
        c = max(a)
        print(c)

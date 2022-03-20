def febonachi(n):
    if n<2:
        return n
    else:
        print(febonachi(n-1),febonachi(n-2))
        return febonachi(n-1)+ febonachi(n-2)

print(febonachi(5))
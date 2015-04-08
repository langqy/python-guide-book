
def dosomething(n):
    if n==0:
        pass
    elif n==1:
        print('do!')
    else:
        print('do!')
        return dosomething(n-1)

print(dosomething(5))


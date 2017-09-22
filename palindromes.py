def main():
    largest=0
    for i in range (100,999):
        for b in range (100,999):
            n=i*b
            if checkpal(n):
                if n>largest:
                    largest=n
                    print1=i
                    print2=b
    print largest
    print print1
    print print2


def checkpal(n):
    num=str(n)
    revnum=num[::-1]
    if num==revnum:
        return True



main()

total=0
for i in range (1,1000):
    if i%3==0:
        total=total+i
    else:
        if i%5==0:
            total=total+i
print total

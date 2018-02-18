def digital_sum(n):
    total=0
    count=0
    while count<len(str(n)):
        total=total+int(str(n)[count])
        count+=1
    return total



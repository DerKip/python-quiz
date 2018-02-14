
def second_largest(li):
    largest=None
    second_largest=None
    for i in range(len(li)):
        if largest==None or li[i]>largest:
            second_largest=largest #second largest initialized with largest value before largest gets updated
            largest=li[i]
    return third_largest




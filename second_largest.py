
def second_largest(li):
    largest=None
    second_largest=None
    for i in range(len(li)):
        if largest==None:
            largest=li[i]
        elif li[i]>largest:
            second_largest=largest #second_largest initialized with largest value before largest gets updated to the next largest element
            largest=li[i]
        elif li[i]>second_largest:
            second_largest=li[i]
    return second_largest

# print(second_largest([2,3,4469,6,565]))   ---For Testing-----




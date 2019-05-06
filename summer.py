def summer(arr):
    if type(arr[0]) == int:
        newstring = sum(arr)
    else:
        newstring = "".join(arr)
    print newstring

summer(['a','b','c'])
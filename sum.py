
def addtwonumbers(arr):
    if (len(arr)==1): return  arr[0]
    return arr[0]+addtwonumbers(arr[1:])

if __name__ == "__main__":
    arr = map(lambda x: int(x), input('please enter elements seperated by spaces:\n\t').split())
    print(addtwonumbers(list(arr)))


#!/usr/bin/python3

def check(arr: list, last: str, first: str) -> bool:
    if arr[0] == last:
        if arr[-1] == first:
            if arr == sorted(arr, reverse=True):
                return False
    return True

def permutation(arr: list) -> None:
    arr_per = sorted(arr)

    last = arr_per[-1]
    first = arr_per[0]

    k = 1
    while check(arr_per, last, first):
        print("".join(arr_per))
        fc = min(arr_per[k:])
        sc = min(arr_per[k+1:])

        arr_per[k+1] = fc
        arr_per[k] = sc

        arr_per[k+1:] = sorted(arr_per[k+1:])
        k = k + 1
        if k == len(arr)-1:
            # print("==>",arr_per)
            k = 1
    return

if __name__ == '__main__':
    string = input("Enter the string: ")

    permutation(string)

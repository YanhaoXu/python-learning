import random


# The function for sorting elements in ascending order

def insertionSort(lst):
    for i in range(1, len(lst)):
        # insert lst[i] into a sorted sublist lst[0 : 1] so that
        # lst[0 : i+1] is sorted
        currentElement = lst[i]
        k = i - 1
        while k >= 0 and lst[k] > currentElement:
            lst[k + 1] = lst[k]
            k -= 1

        # Insert the current element into lst[k + 1]
        lst[k + 1] = currentElement


def main():
    lst = []
    for i in range(20):
        lst.append(random.randint(1, 100))

    print("bef", lst)

    insertionSort(lst)

    print("sort", lst)


main()

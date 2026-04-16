from math import floor

def comb_sort(arr: list):
    # initial gap
    gap = len(arr)
    SHRINK_FACTOR = 1.3
    sorted = False

    while sorted == False:
        gap = floor(gap / SHRINK_FACTOR)
        if gap <= 1:
            gap = 1
            sorted = True
        # "rule of 11" by Lacey and Box
        elif gap == 9 or gap == 10:
            gap = 11

        i = 0
        while (i + gap) < len(arr):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1

# for comparison
def bubble_sort(arr: list):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

if __name__ == '__main__':
    from random import randint, uniform
    import time
    int_list_1 = [randint(-50, 50) for _ in range(50)]
    int_list_2 = [randint(-3000, 3000) for _ in range(3000)]
    float_list_1 = [uniform(-50.0, 50.0) for _ in range(50)]
    float_list_2 = [uniform(-3000.0, 3000.0) for _ in range(3000)]

    for l in (int_list_1, int_list_2, float_list_1, float_list_2):
        start = time.perf_counter()
        bubble_sort(l.copy())
        end = time.perf_counter()
        print(f'Bubble Sort: {end - start:.6f} seconds')
        start = time.perf_counter()
        comb_sort(l.copy())
        end = time.perf_counter()
        print(f'Comb Sort: {end - start:.6f} seconds')
        print('')

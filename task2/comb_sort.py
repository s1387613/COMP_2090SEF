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

if __name__ == '__main__':
    from random import randint, uniform
    int_list_1 = [randint(-50, 50) for _ in range(50)]
    int_list_2 = [randint(-3000, 3000) for _ in range(3000)]
    float_list_1 = [uniform(-50.0, 50.0) for _ in range(50)]
    float_list_2 = [uniform(-3000.0, 3000.0) for _ in range(3000)]

    for l in (int_list_1, int_list_2, float_list_1, float_list_2):
        comb_sort(l)

    print(f'int_list_1:   {int_list_1 == sorted(int_list_1)}')
    print(f'int_list_2:   {int_list_2 == sorted(int_list_2)}')
    print(f'float_list_1: {float_list_1 == sorted(float_list_1)}')
    print(f'float_list_2: {float_list_2 == sorted(float_list_2)}')

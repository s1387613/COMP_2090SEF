# COMP_2090SEF

## Task 1
A personal finance management program, allowing user to keep track of their expense.

### Quick start
> [!NOTE]
> Some installtion of Python does not have TKinter preinstalled
```
git clone https://github.com/s1387613/COMP_2090SEF.git
cd COMP_2090SEF/task1
python3 interface.py
```

### Features
* Full GUI support for transactions
* History of all transactions
* Real-time updated balance value

### Tests
For simple test cases, you can run the Python files itself.

## Task 2
Data structure: hashed array tree

Hashed Array Tree is a dynamic array data structure that offers high performance and flexibility like a standard dynamic array, while being more memory efficient as only necesary memory is allocated.

HAT is often used it memory constrainted situations while needing the flexibility of a dynamic array, such as embedded systems and file systems implementation.

|lookup|mutate (start)|mutate (end)|resize|  -   |wasted space|
|:-----|:-------------|:-----------|:-----|:-----|:-----------|
|O(1)  |O(n)          |O(1)        |O(n)  |  -   |O(sqrt(n))  |

Algorithm: Comb Sort

Comb Sort is an improvement over the popular Bubble Sort, with the main difference being Comb Sort has a varying gap size in element comparison that depends on a shrink factor, where Bubble Sort has a fixed gap size of 1.

This special feature of Comb Sort allows it to eliminate small values near the end of the list early on, without having to wait for gap=1 iterations. Thus, Comb Sort generally offers better performance compared to Bubble Sort.

|best case|average case|worst case|
|:--------|:-----------|:---------|
|O(nlog n)|O(n^2 / 2^p)|O(n^2)    |

### Quick start
```
git clone https://github.com/s1387613/COMP_2090SEF.git
cd COMP_2090SEF/task2
```
> [!NOTE]
> This is a simple test comparing Comb Sort against Bubble Sort, the result is not conclusive and might not apply to other situations

For testing Comb Sort:
```
python3 comb_sort.py
```
> [!NOTE]
> Since there is no pointer in Python, the HAT is implemented as a 2-dimensional array

For testing Hashed Array Tree:
```
python3 hash_array_tree.py
```

### Demo
> [!NOTE]
> If your media player does not support webm format, try dragging the video into the browser window and play it in the browser.

https://github.com/s1387613/COMP_2090SEF/blob/main/task2/task2.webm

from table import Table
from data import Data
import pygame


class Algorithm:
    def __init__(self, algo, win=None):
        self.algo = algo
        self.win = win

    def run(self, table):
        if self.algo == "Insertion Sort":
            return self.insertion_sort(table)
        if self.algo == "Quick Sort":
            return self.quick_sort(table)
        if self.algo == "Fusion Sort":
            return self.fusion_sort(table)
        if self.algo == "Bubble Sort":
            return self.bubble_sort(table)

    def insertion_sort(self, table):
        n = len(table.data)
        for i in range(n):
            value = table.data[i].value
            j = i
            while j > 0 and table.data[j - 1].value > value:
                table.data[j] = Data(table.data[j - 1].value, (255, 120, 120))
                table.draw()
                # table.data[j].set_color()
                j -= 1

            for e in range(j, i):
                table.data[e].set_color()

            table.data[j] = Data(value, (255, 120, 120))
            table.draw()

            table.data[j].set_color()
        table.draw()

    def quick_sort(self, table):
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]
            table.data[i].set_color((255, 120, 120))
            table.data[j].set_color((255, 120, 120))
            table.draw()
            table.data[i].set_color()
            table.data[j].set_color()
            return arr

        def partition(arr, low, high):
            i = low - 1
            pivot = arr[high].value

            table.data[high].set_color((255, 255, 100))
            table.draw()

            for j in range(low, high):
                if arr[j].value <= pivot:
                    i = i + 1
                    arr = swap(arr, i, j)

            arr = swap(arr, i + 1, high)

            table.data[high].set_color()
            return i + 1

        def quickSort(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                arr = quickSort(arr, low, pi - 1)
                arr = quickSort(arr, pi + 1, high)
            return arr

        return quickSort(table.data, 0, len(table.data) - 1)

    def bubble_sort(self, table):
        for i in range(len(table.data) - 1, 0, -1):
            sorted_ = True
            table.data[i].set_color((255, 255, 120))
            for j in range(0, i):
                if table.data[j + 1].value < table.data[j].value:
                    table.data[j + 1], table.data[j] = table.data[j], table.data[j + 1]
                    sorted_ = False

                    table.data[j + 1].set_color((255, 120, 12))
                    table.draw()
                    # pygame.time.delay(300)
                    table.data[j + 1].set_color()

            table.data[i].set_color()
            if sorted_:
                return


"""
    def fusion_sort(self, table):
        def fusion(A, B):
            from time import sleep

            sleep(0.2)
            if len(A) == 0:
                return B
            if len(B) == 0:
                return A

            A[0].set_color((255, 120, 120))
            B[0].set_color((255, 120, 120))
            table.draw()
            A[0].set_color()
            B[0].set_color()

            if A[0].value <= B[0].value:
                return [A[0]] + fusion(A[1:], B)
            return [B[0]] + fusion(A, B[1:])

        def _fusionsort(array):
            N = len(array)
            if len(array) <= 1:
                return array
            return fusion(
                _fusionsort(array[: int(N / 2)]), _fusionsort(array[int(N / 2) + 1 :])
            )

        a = _fusionsort(table.data)
        print([i.value for i in a])
        return a

    def merge_sort(self, table):
        def fusion(A, B):
            if len(A) == 0:
                return B
            if len(B) == 0:
                return A

            A[0].set_color((255, 120, 120))
            B[0].set_color((255, 120, 120))
            table.draw()
            A[0].set_color()
            B[0].set_color()

            if A[0].value <= B[0].value:
                return [A[0]] + fusion(A[1:], B)
            return [B[0]] + fusion(A, B[1:])

        def _fusionsort(i=0, j=len(table.data) - 1):
            N = j + 1
            if N <= 1:
                if N == 0:
                    return []
                return [table.data[i]]
            return fusion(_fusionsort(0, int(N / 2)), _fusionsort(int(N / 2) + 1, N))

        def merge(table, (beg1, last1), (beg2, last2)):
            if len(table.data[beg1:last1]) == 0:
                return _
            if len(table.data[beg2:last2]) == 0:
                return _

            table.data[beg1].set_color((255, 120, 120))
            table.data[beg2].set_color((255, 120, 120))
            table.draw()
            table.data[beg1].set_color()
            table.data[beg2].set_color()

        def splitter(table, i=0, j=len(table.data)):
            N = j + 1
            if N <= 1:
                return (i, N)
            return merge(
                table,
                splitter(table, 0, int(N / 2) + 1),
                splitter(table, int(N / 2) + 1, N + 1),
            )

        return splitter(table)
"""


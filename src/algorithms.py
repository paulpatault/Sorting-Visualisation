from table import Table
from data import Data


class Algorithm:
    def __init__(self, algo):
        self.algo = algo

    def run(self, table):
        if self.algo == "Insertion Sort":
            return self.insertion_sort(table)
        if self.algo == "Quick Sort":
            return self.quick_sort(table)

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

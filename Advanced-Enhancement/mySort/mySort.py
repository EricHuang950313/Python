import random

class mySort():
    def __init__(self, r):
        self.range = r
        l = [i for i in range(1, self.range+1)]
        random.shuffle(l)
        print(f"Randomized list: {l}")
        self.l = l


    def check(self, toCheck):
        for i in range(len(toCheck)-1):
            if toCheck[i] > toCheck[i+1]:
                break
            else:
                pass
        else:
            return True
        return False


    def selection_sort(self):
        toSort = [i for i in self.l]
        for i in range(len(toSort)-1):
            if self.check(toSort) == True:
                if i == 0:
                    print("None")
                break
            value, index = toSort[i:][0], i
            for j in range(len(toSort[i:])):
                if toSort[i+j] < value:
                    value, index = toSort[i+j], i+j
                else:
                    pass
            toSort.insert(i, toSort[index])
            toSort.pop(index+1)
            print(f"Process: step{i+1}, {toSort}")


    def insertion_sort(self):
        toSort = [i for i in self.l]
        for i in range(1, len(toSort)):
            if self.check(toSort) == True:
                if i == 1:
                    print("None")
                break
            for j in range(i-1, -1, -1):
                if j == 0 and toSort[i] < toSort[j]:
                    toSort.insert(j, toSort[i])
                    toSort.pop(i+1)
                    break
                elif toSort[i] < toSort[j] and toSort[i] > toSort[j-1]:
                    toSort.insert(j, toSort[i])
                    toSort.pop(i+1)
                    break
                else:
                    pass
            print(f"Process: step{i}, {toSort}")


    def bubble_sort(self):
        toSort = [i for i in self.l]
        if self.check(toSort) == True:
            print("None")
        else:
            move = 0
            for i in range(len(toSort)-1):
                for j in range(0, len(toSort)-1-i):
                    if toSort[j] > toSort[j+1]:
                        toSort[j], toSort[j+1] = toSort[j+1], toSort[j]
                        move += 1
                        print(f"Process: move{move}, {toSort}")
                    else:
                        pass
            

if __name__ == "__main__":
    print("===Init(Set a range to generate a random list)===")
    simulation = mySort(10)       
    print("===Selection Sort===")
    simulation.selection_sort()
    print("===Insertion Sort===")
    simulation.insertion_sort()
    print("===Bubble Sort===")
    simulation.bubble_sort()
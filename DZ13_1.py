import random
import time
from random_word import RandomWords
str_list=[]
r=RandomWords()

while len(str_list)<5:
    str_list.append(r.get_random_word())
print(str_list)
                                            #Список з цілими часлами
int_list=[]
while len(int_list)<5000:
    x=random.randrange(0,1000)
    int_list.append(x)
print(int_list)

                                            #Список чисел з комою
float_list=[]
while len(float_list)<5000:
    x=random.uniform(0.1,100)
    float_list.append(x)
print(float_list)

                                            #Список слів

def bubble_sort(data):
    length=len(data)
    for iIndex in range(length):
        swapped=False
        for jIndex in range(0, length - iIndex - 1):
            if data[jIndex]>data[jIndex+1]:
                data[jIndex], data[jIndex+1] = data[jIndex+1], data[jIndex]
                swapped=True
        if not swapped:
            break
    print('bubble sort', data)
start_time=time.time()
bubble_sort(str_list)
print(time.time()-start_time)

def selection_sort(data):
    for scanIndex in range(0, len(data)):
        minIndex=scanIndex
        for compIndex in range(scanIndex+1, len(data)):
            if data[compIndex]<data[minIndex]:
                minIndex=compIndex
        if minIndex!=scanIndex:
            data[scanIndex], data[minIndex]=data[minIndex], data[scanIndex]
    print('selection sort ',data)
start_time=time.time()
selection_sort(float_list)
print(time.time()-start_time)

def insertion_sort(data):
    for scanIndex in range(1, len(data)):
        tmp=data[scanIndex]
        minIndex=scanIndex
        while minIndex>0 and tmp<data[minIndex-1]:
            data[minIndex]=data[minIndex-1]
            minIndex-=1
        data[minIndex]=tmp
    print('Insertion sort ',data)
start_time=time.time()
insertion_sort(int_list)
print(time.time()-start_time)
import numpy as np
def part(left, right, arr, ax, arr_label):
    i = left - 1
    for j in range(left, right):
        if arr[j][ax] < arr[right][ax]:
            i += 1
            tmp = np.array(arr[i])
            arr[i] = arr[j]
            arr[j] = tmp
            
            tmp = arr_label[i]
            arr_label[i] = arr_label[j]
            arr_label[j] = tmp
    i += 1
    tmp = np.array(arr[i])
    arr[i] = arr[right]
    arr[right] = tmp
    
    tmp = arr_label[i]
    arr_label[i] = arr_label[right]
    arr_label[right] = tmp    
    
    return [i, arr, arr_label]

def qsort(left, right, arr, ax, arr_label):
    if left < right:
        [q, arr, arr_label] = part(left, right, arr, ax, arr_label)
        [arr, arr_label] = qsort(left, q-1, arr, ax, arr_label)
        [arr, arr_label] = qsort(q+1, right, arr, ax, arr_label)
        return [arr, arr_label]
    else:
        return [arr, arr_label]


#a = np.array([[3,-1],[2,-3],[1,0]])
#ay = np.array([0,1,2])
#b, by = qsort(0, len(a)-1 , a, 1, ay)
#print(b, by)


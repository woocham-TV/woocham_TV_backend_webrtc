arr = [17, 28, 43, 67, 88, 92, 100]
target = 92
mid = arr[int(len(arr) / 2)]
low = 0
high = len(arr) - 1

while(low <= high):
    mid = int((low + high) / 2)
    
    if arr[mid] == target:
        print(mid)
        break
    elif arr[mid] > target:
        high = mid - 1
    else:
        low = mid + 1
    
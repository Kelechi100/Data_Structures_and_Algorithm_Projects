#How to tranfrom a List to a heap
import heapq
data = [1,2,3,8,8,10,4]
heapq.heapify(data)
print(data)
# adding new elements to the heap
heapq.heappush(data, 0)
print(data)

# removing new elements from the heap
print(heapq.heappop(data))
print(data)
# pushin a new item and poping the smallest item
print(heapq.heappushpop(data, 3))
print(data)
#repalcing the smallest item and push a new item
print(heapq.heapreplace(data, 3))
print(data)
print(heapq.nlargest(3, data))
print(heapq.nsmallest(3, data))

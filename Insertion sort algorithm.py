# Python program fpr implemtation of insertion sort
# function to do insertion sort
def insertSort(arr):
	#Traverse through 1 to len(arr)
	for i in range(1,len(arr)):
		key=arr[i]
		#Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
		j=i-1
		while j>=0 and key<arr[j]:
			arr[j+1]=arr[j]
			j-=1
		arr[j+1]=key
# sorting the array[13,45,6,1,3,4,8,9,10] usinf insertionsort
arr=[13,45,6,1,3,4,8,9,10]
print(f"arrays Before been Sorted: {arr}")
insertSort(arr)
list = [] # created empty list to store sorted array elemnys
print("Sorted array is:")
for i in range(len(arr)):
	list.append(arr[i]) # appending the sorted array elements to the list
	print(list)
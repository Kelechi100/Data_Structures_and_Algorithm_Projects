from dynamicArray import MydynamicArray
# Testing the dyanamic arrays method
if  __name__ == "__main__":
    # Creating an empty array
    my_array = MydynamicArray()
    print("Testing append:")
    my_array.append(20)
    my_array.append(25)
    my_array.append(30)
    my_array.append(35)
    my_array.append(40)
    my_array.append(45)
    print("Original array", my_array)
    print("\nTesting insert:")
    my_array.insert(1,15)
    print("After inserting at index 1 with value 15:\n",my_array)
    print("\nTesting remove:")
    my_array.remove_item(30)
    print("After removing item 30:\n",my_array)
    print("\nTesting popping:")
    popped_item = my_array.pop()
    print(f'popped item is {popped_item}')
    print(f"Array after popping item{my_array}")
    
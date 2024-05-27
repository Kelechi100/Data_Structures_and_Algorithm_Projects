from Node import CircularQueue

def  hot_potato_game(n,k):
    if n <= 0:
        return None
    
    queue = CircularQueue()
    for i in range(1, n + 1):
        queue.enqueue(i)
    
    print("Circle")
    queue.print_queue()

    while queue.get_size() > 1:
        queue.rotate(k)
        eliminated = queue.dequeue()
        print(f"Eliminated: {eliminated} ")
        print("Remaining")
        queue.print_queue()
        

    return queue.dequeue()

n = int(input("Enter the number of people (n): "))
k = int(input("Enter counting interval (k): "))
winner = hot_potato_game(n, k)
print(f"The winner is: {winner}")
print(f"The last remaining Person is at position: {winner}")
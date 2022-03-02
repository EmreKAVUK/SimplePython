queue = []
#adding variable it's called EnQueue
queue.append('apple')
queue.append(23)
queue.append('c')
print(len(queue))
print("Initial queue")
print(queue)
#Remove variable it's called deQueue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)
print(queue.size()a
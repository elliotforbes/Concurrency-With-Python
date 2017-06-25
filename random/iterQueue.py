import queue

myQueue = queue.Queue()

myQueue.put(2)
myQueue.put(3)
myQueue.put(4)

for job in iter(myQueue.get, None):
  print(job)


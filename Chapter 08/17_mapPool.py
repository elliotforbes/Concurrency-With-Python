from multiprocessing import Pool
import time

def myTask(n):
  time.sleep(n/2)
  return n*2

def main():
  with Pool(4) as p:
     iterable = p.imap_unordered(myTask, [4,3,2,1])
     print(next(iterable))
     print(next(iterable))
     print(next(iterable))
     print(next(iterable))

if __name__ == '__main__':
  main()

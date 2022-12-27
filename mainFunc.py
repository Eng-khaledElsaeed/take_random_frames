
from randomframes import producer , consumer
from queue import Queue

if __name__ == '__main__':
      queue=Queue()
      pFolder =r'C:\Users\Khale\Desktop\Documents\memories\VID_20210222_213503.mp4'
      C = consumer(queue)
      P = producer(pFolder,queue)
      P.start()
      C.start()



                
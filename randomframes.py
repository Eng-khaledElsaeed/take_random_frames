import threading
import os
import cv2
# -----------------------------------

# poducer 
class producer(threading.Thread):
    def __ini__(self,path,queue):
        self.queue=queue
        self.path=path
        super(producer, self).__init__()

    def run(self):
        for root,dirs,files in os.walk(self.path):
            for file in files:
                vid=cv2.VideoCapture(str(self.path)+'\\'+str(file))
                self.queue.append(str(file),vid)



class consumer(threading.Thread):
    def __init__(self,queue):
        self.queue=queue
        super(consumer, self).__init__()

    def run(self):
        name,videostream=self.queue.pop()
        self.randomframs(name,videostream)


    def randomframs(self,name,videostreams):
        name=self.queue[0]
        self.queue.pop()
        if not os.path.exists(str(self.path)+'\\'+str(name)+'frams'):
            os.makedirs(str(self.path)+'\\'+str(name)+'frams')
        framecounter=0
        while(True):
            sucess,image=videostreams.read()
            frame = cv2.rotate(image, cv2.ROTATE_180)
            cv2.imshow("outpot",frame)
            cv2.waitKey(1)
            framecounter +=1
            if framecounter % 15 == 0:
                cv2.imwrite(str(self.path)+'\\'+str(name)+'frames'+'\\frame' + str(framecounter/15) +'.jpg', frame)
                print(frame)

            videostreams.release()
            cv2.destroyAllWindows()


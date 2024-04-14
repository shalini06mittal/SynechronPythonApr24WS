import logging
import time
import threading

#task the thread will perfoem
def thread_f1(name,c):
    print('Thread  starting',name,c)
    time.sleep(2)
    print('Thread  finish', name)


if __name__ == '__main__':
    print(' main : brefore creating thread')
    x = threading.Thread(target=thread_f1, args=[1,5], daemon=True)
    print('Main - before running thread')
    x.start()
    print('Main - after running thread')
    #x.join()
    print('Main - all done')

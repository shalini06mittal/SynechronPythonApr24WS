import threading
import time 
def thread_f1(name, start):
    print(name , 'Thread start')
    for i in range(start, start+5):
        print('Thread',name,'->',i)
        time.sleep(2)
    print(name , 'Thread end')

    
threads = []
for index in range(3):
    x = threading.Thread(target=thread_f1, args=[index+1, index+5])
    threads.append(x)
    x.start()

# for index, thread in enumerate(threads):
#     pass
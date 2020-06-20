import threading
import time
def thread_work():
    print("haisd\n")
    for i in range(5):
        time.sleep(0.1)
    print("finish\n")
def thread_job():
    print("T1 START\n")
    for i in range(10):
        time.sleep(0.1)
    print("T1 FINISH\n")
def thread():
    added_thread = threading.Thread(target=thread_job, name='T1')
    b = threading.Thread(target=thread_work)
    added_thread.start()
    b.start()
    added_thread.join()
    print("all done\n")

if __name__ == '__main__':
    thread()


import threading
import time

def thread_job():
    print('This is a new threading job, number is %s' % threading.current_thread())

def T1():
    print('threading_t1 start')
    print('threading_t1 finsh')

def T2():
    print('threading_t2 start')
    for i in range(10):
        time.sleep(0.5)
    print('threading_t2 finsh')

def main():
    TH1 = threading.Thread(target=T1(), name='T1')
    TH2 = threading.Thread(target=T2())
    TH2.start()
    TH2.join()
    TH1.start()
    print("all done\n")

    # print(threading.active_count()) #活跃的线程量
    # print(threading.current_thread()) #当前线程
    # print(threading.enumerate()) #线程列表


if __name__ == '__main__':
    main()
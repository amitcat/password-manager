from time import sleep
from threading import Thread


class coustomThread(Thread):
    def run(self):
        sleep(1)
        print('this is coming from a thread')


def task(sleep_time, message):
    sleep(sleep_time)
    print(message)


def main():
    # thread1 = Thread(target=task, args=(1, 'hello world1 \n'))
    # thread1.start()
    # # print(thread1.getName())
    # thread1.join()
    #
    # thread2 = Thread(target=task, args=(1, 'hello world2 \n'))
    # thread2.start()
    # # print(thread2.getName())
    # thread2.join()
    thread1 = coustomThread()
    thread1.start()
    thread2 = coustomThread()
    thread2.start()


main()

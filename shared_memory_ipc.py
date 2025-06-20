from multiprocessing import Process, Value, Lock

def producer(shared_value, lock):
    with lock:
        shared_value.value += 1
        print(f"Produced value: {shared_value.value}")

def consumer(shared_value, lock):
    with lock:
        print(f"Consumed value: {shared_value.value}")
        shared_value.value -= 1

def run_ipc_demo():
    shared_value = Value('i', 0)
    lock = Lock()
    p1 = Process(target=producer, args=(shared_value, lock))
    p2 = Process(target=consumer, args=(shared_value, lock))
    p1.start()
    p1.join()
    p2.start()
    p2.join()

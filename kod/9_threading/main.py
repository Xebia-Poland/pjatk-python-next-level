import threading

counter = 0

def worker():
    """My job is to increment current counter and print the current count"""
    global counter

    counter += 1
    print(f'Count is {counter}')
    # introduce some noise to increase chance of creating race condition
    print('--------------------')

print('Starting up')
for i in range(10):
    threading.Thread(target=worker).start()
print('finishing up')


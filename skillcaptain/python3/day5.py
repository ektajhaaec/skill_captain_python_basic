import threading

def message1():
    print("this is the first message")

def message2():
    print("this is the second message")

def message3():
    print("this is the third message")

first_message = threading.Thread(target =message1)
second_message = threading.Thread(target =message2)
third_message = threading.Thread( target =message3)

first_message.start()
second_message.start()
third_message.start()

first_message.join()
second_message.join()
third_message.join()

import sys

from MessageQueue import MessageQueue

def Usage():
    print("Usage")

def Start(mq):
    while (True):
        msg = input("Enter msg")
        mq.sendMessage(msg)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please provide host of RabbitMQ Queue server")
        sys.exit(1)

    messageServerHost = sys.argv[1]
    mq = MessageQueue(messageServerHost)
    if mq.establishConnection():
        while True:
            msg = input("Please type a message")
            mq.sendMessage(msg)

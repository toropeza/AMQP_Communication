import sys

from MessageQueue import MessageQueue

def Usage():
    print("Usage")

def Start(mq):
    while (True):
        msg = input("Enter msg")
        mq.sendMessage(msg)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Please provide host of RabbitMQ Queue server")
        sys.exit(1)
    print("Waiting for a message")
    messageServerHost = sys.argv[1]
    mq = MessageQueue(messageServerHost)
    if mq.establishConnection():
        mq.listen(callback)

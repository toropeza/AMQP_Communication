import pika

class MessageQueue:
    rpsChannelKey = "rps"

    def __init__(self, host):
        self.host = host

    def establishConnection(self):
        self.pikaConnection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
        self.rpsChannel = self.pikaConnection.channel()
        self.rpsChannel.queue_declare(queue=self.rpsChannelKey)

        if self.pikaConnection == None or self.rpsChannel == None:
            return False
        return True

    def listen(self, callback):
        self.rpsChannel.basic_consume(callback,
                      queue=self.rpsChannelKey,
                      no_ack=True)
        self.rpsChannel.start_consuming()

    def sendMessage(self, msg):
        self.rpsChannel.basic_publish(exchange='',
                          routing_key=self.rpsChannelKey,
                          body=msg)
        print(" [x] Sent '" + msg + "'")

    def closeConnection(self):
        if self.pikaConnection != None:
            self.pikaConnection.close()
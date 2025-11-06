# --- FILE : chat_receive.py ---
import pika
import sys

CLOUDAMQP_URL = "amqps://bdpuodkw:HFZokWmUMSAdGLkUR6yS4dWdeUVkaK9Z@kebnekaise.lmq.cloudamqp.com/bdpuodkw"

def start_chat_client(username):
    connection = pika.BlockingConnection(pika.URLParameters(CLOUDAMQP_URL))
    channel = connection.channel()
    channel.exchange_declare(exchange='chat_room', exchange_type='fanout')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='chat_room', queue=queue_name)

    print(f"[*] {username} joined the chat. To exit press CTRL+C\n")

    def callback(ch, method, properties, body):
        print(body.decode())

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python chat_receive.py <username>")
        sys.exit(1)
    username = sys.argv[1]
    start_chat_client(username)

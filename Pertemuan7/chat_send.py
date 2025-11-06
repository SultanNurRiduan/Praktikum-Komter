# --- FILE : chat_send.py ---
import pika
import sys

CLOUDAMQP_URL = "amqps://bdpuodkw:HFZokWmUMSAdGLkUR6yS4dWdeUVkaK9Z@kebnekaise.lmq.cloudamqp.com/bdpuodkw"

def send_message(username, message):
    connection = pika.BlockingConnection(pika.URLParameters(CLOUDAMQP_URL))
    channel = connection.channel()
    channel.exchange_declare(exchange='chat_room', exchange_type='fanout')

    full_message = f"{username}: {message}"
    channel.basic_publish(exchange='chat_room', routing_key='', body=full_message)
    connection.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python chat_send.py <username> <message>")
        sys.exit(1)
    username = sys.argv[1]
    message = ' '.join(sys.argv[2:])
    send_message(username, message)
    print(f"[x] Sent: {username}: {message}")

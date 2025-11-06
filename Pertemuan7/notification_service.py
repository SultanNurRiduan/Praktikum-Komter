# --- FILE : notification_service.py ---
import pika
import json

CLOUDAMQP_URL = "amqps://bdpuodkw:HFZokWmUMSAdGLkUR6yS4dWdeUVkaK9Z@kebnekaise.lmq.cloudamqp.com/bdpuodkw"

connection = pika.BlockingConnection(pika.URLParameters(CLOUDAMQP_URL))
channel = connection.channel()

channel.queue_declare(queue='notifications')

def process_notification(ch, method, properties, body):
    data = json.loads(body.decode())
    print(f"[x] Processing notification:")
    print(f"User ID : {data['user_id']}")
    print(f"Message : {data['message']}")
    print(f"Time : {data['timestamp']}\n")

channel.basic_consume(
    queue='notifications',
    on_message_callback=process_notification,
    auto_ack=True
)

print('[*] Waiting for notifications. To exit press CTRL+C')
channel.start_consuming()

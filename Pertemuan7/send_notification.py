# --- FILE : send_notification.py ---
import pika
import json
from datetime import datetime

CLOUDAMQP_URL = "amqps://bdpuodkw:HFZokWmUMSAdGLkUR6yS4dWdeUVkaK9Z@kebnekaise.lmq.cloudamqp.com/bdpuodkw"

def send_notification(user_id, message):
    connection = pika.BlockingConnection(pika.URLParameters(CLOUDAMQP_URL))
    channel = connection.channel()

    channel.queue_declare(queue='notifications')

    notification = {
        'user_id': user_id,
        'message': message,
        'timestamp': datetime.now().isoformat()
    }

    channel.basic_publish(
        exchange='',
        routing_key='notifications',
        body=json.dumps(notification)
    )

    print(f"[x] Sent notification to user {user_id}")
    connection.close()

if __name__ == '__main__':
    send_notification(123, "Pesanan Anda sudah dikirim!")
    send_notification(456, "Ada pesan baru untuk Anda")

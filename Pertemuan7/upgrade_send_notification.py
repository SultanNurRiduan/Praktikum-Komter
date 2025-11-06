# --- FILE : upgrade_send_notification.py ---
import pika
import json
from datetime import datetime

CLOUDAMQP_URL = "amqps://bdpuodkw:HFZokWmUMSAdGLkUR6yS4dWdeUVkaK9Z@kebnekaise.lmq.cloudamqp.com/bdpuodkw"

def send_notification(user_id, message):
    # Koneksi ke RabbitMQ
    connection = pika.BlockingConnection(pika.URLParameters(CLOUDAMQP_URL))
    channel = connection.channel()

    # Buat queue yang tahan crash (durable)
    channel.queue_declare(queue='notifications_v2', durable=True)

    # Data notifikasi dalam format JSON
    notification = {
        'user_id': user_id,
        'message': message,
        'timestamp': datetime.now().isoformat()
    }

    # Publish pesan JSON dengan properti durable
    channel.basic_publish(
        exchange='',
        routing_key='notifications_v2',
        body=json.dumps(notification),
        properties=pika.BasicProperties(
            delivery_mode=2  # 2 = persistent (pesan tidak hilang kalau RabbitMQ crash)
        )
    )

    print(f"[x] Sent notification to user {user_id}")
    connection.close()

if __name__ == '__main__':
    send_notification(123, "Pesanan Anda sudah dikirim!")
    send_notification(456, "Ada pesan baru untuk Anda")

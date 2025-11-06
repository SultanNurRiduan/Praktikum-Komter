# --- FILE : upgrade_notification_service.py ---
import pika
import json
import time

CLOUDAMQP_URL = "amqps://bdpuodkw:HFZokWmUMSAdGLkUR6yS4dWdeUVkaK9Z@kebnekaise.lmq.cloudamqp.com/bdpuodkw"

# Koneksi ke RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(CLOUDAMQP_URL))
channel = connection.channel()

# Queue dibuat durable agar tidak hilang saat crash
channel.queue_declare(queue='notifications_v2', durable=True)

def process_notification(ch, method, properties, body):
    try:
        # Parse JSON dari pesan
        data = json.loads(body.decode())

        print(f"[x] Processing notification:")
        print(f"User ID : {data['user_id']}")
        print(f"Message : {data['message']}")
        print(f"Time : {data['timestamp']}\n")

        # Simulasi proses lama
        time.sleep(5)

        # Manual acknowledgment (tanda pesan sudah diproses)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        print("[✓] Notification processed successfully.\n")

    except json.JSONDecodeError:
        # Jika pesan tidak valid JSON
        print(f"[!] Invalid JSON message skipped: {body}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

# Jalankan consumer tanpa auto_ack
channel.basic_consume(
    queue='notifications_v2',
    on_message_callback=process_notification
)

print('[*] Waiting for notifications. To exit press CTRL+C')
channel.start_consuming()

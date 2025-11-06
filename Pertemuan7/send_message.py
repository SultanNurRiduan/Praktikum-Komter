# --- FILE : send_message.py ---
import pika

CLOUDAMQP_URL = "amqps://bdpuodkw:HFZokWmUMSAdGLkUR6yS4dWdeUVkaK9Z@kebnekaise.lmq.cloudamqp.com/bdpuodkw"

# Koneksi ke RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(CLOUDAMQP_URL))
channel = connection.channel()

# Buat queue
channel.queue_declare(queue='hello')

# Kirim pesan
message = "Hello, Mata kuliah Komputasi Paralel dan Terdistribusi! pesan 2"
channel.basic_publish(
    exchange='',
    routing_key='hello',
    body=message
)

print(f"[x] Sent '{message}'")
connection.close()

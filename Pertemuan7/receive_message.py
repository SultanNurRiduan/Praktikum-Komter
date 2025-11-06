# --- FILE : receive_message.py ---
import pika

CLOUDAMQP_URL = "amqps://bdpuodkw:HFZokWmUMSAdGLkUR6yS4dWdeUVkaK9Z@kebnekaise.lmq.cloudamqp.com/bdpuodkw"

# Koneksi ke RabbitMQ
connection = pika.BlockingConnection(pika.URLParameters(CLOUDAMQP_URL))
channel = connection.channel()

# Pastikan queue ada
channel.queue_declare(queue='hello')

# Callback saat pesan diterima
def callback(ch, method, properties, body):
    print(f"[x] Received {body.decode()}")

channel.basic_consume(
    queue='hello',
    on_message_callback=callback,
    auto_ack=True
)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

# --- FILE : new_task.py ---
import pika
import sys

CLOUDAMQP_URL = "amqps://bdpuodkw:HFZokWmUMSAdGLkUR6yS4dWdeUVkaK9Z@kebnekaise.lmq.cloudamqp.com/bdpuodkw"

connection = pika.BlockingConnection(pika.URLParameters(CLOUDAMQP_URL))
channel = connection.channel()

# Buat queue yang tahan restart
channel.queue_declare(queue='task_queue', durable=True)

# Ambil pesan dari argumen command-line
message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2,  # Persistent message
    )
)

print(f"[x] Sent '{message}'")
connection.close()

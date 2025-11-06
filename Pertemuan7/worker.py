# --- FILE : worker.py ---
import pika
import time

CLOUDAMQP_URL = "amqps://bdpuodkw:HFZokWmUMSAdGLkUR6yS4dWdeUVkaK9Z@kebnekaise.lmq.cloudamqp.com/bdpuodkw"

connection = pika.BlockingConnection(pika.URLParameters(CLOUDAMQP_URL))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    message = body.decode()
    print(f"[x] Received {message}")
    time.sleep(message.count('.'))  # simulasi kerja
    print("[x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Fair dispatch
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

print('[*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

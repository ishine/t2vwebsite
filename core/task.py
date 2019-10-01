from celery.decorators import task
import pika


@task()
def voice_generator_server():

    # Declaring connection and chenal and queue
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='rpc_queue')

    # callback method
    def on_request(ch, method, props, body):
        # action
        text = body.decode('utf-8')

        # sending response back
        ch.basic_publish(exchange='',
                         routing_key=props.reply_to,
                         properties=pika.BasicProperties(
                             correlation_id=props.correlation_id),
                         body=str(text))
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # start consuming
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(on_message_callback=on_request, queue='rpc_queue')

    channel.start_consuming()

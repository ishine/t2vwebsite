from celery.decorators import task
from django.dispatch import receiver
import time
import pika
import datetime



@task()
def hello_task():
	def on_message(channel, method_frame, header_frame, body):
	    
	    print("received " + body.decode('utf-8'))
	    print(datetime.datetime.now())
	    channel.basic_ack(delivery_tag=method_frame.delivery_tag)
	    

	# declarint connection and chenel
	connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
	channel = connection.channel()

	# get massage
	channel.queue_declare(queue='rabbit')
	
	channel.basic_consume(queue='rabbit', on_message_callback=on_message)
		
	channel.start_consuming()


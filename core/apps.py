from django.apps import AppConfig
from .task import hello_task

class CoreConfig(AppConfig):
	name = 'core'

	def ready(self):
		print("ready run")
		hello_task.delay()
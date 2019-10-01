from django.apps import AppConfig
from .task import voice_generator_server


class CoreConfig(AppConfig):
	name = 'core'

	def ready(self):
		voice_generator_server.delay()

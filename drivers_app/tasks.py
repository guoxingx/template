# coding: utf-8

import time

from celery import Celery

from config import config
from seeker import run_carbens_spider


config_name = 'test'
broker = config[config_name].REDIS_URL
celery = Celery('drivers', broker=broker)


@celery.task(bind=True)
def grab_carbens(self):
    print('run grab_carbens(). self: {}, {}'.format(self, type(self)))

    run_carbens_spider()

    self.update_state(state='PROGRESS', meta={'status': 'progressing'})
    time.sleep(1)

    return {'status': 'complete'}

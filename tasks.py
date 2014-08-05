#!/usr/bin/env python
from celery import Celery

app = Celery('tasks', backend = 'redis://localhost:6379/0', 
             broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    return x + y

result = add.delay(4, 4)
if result.ready():
    print result.result
# api/tasks.py

from typing import List
import time, random

from celery import shared_task

@shared_task
def print_hello_task():
    rand_num = random.randint(1, 5)
    return f'Hello, user{rand_num}'

@shared_task
def test_task(a: int, b: int):
    print("test Celery task : ", a + b)
    return a + b

@shared_task
def test_periodic_task():
    print("test Periodic task")
    return "Complete"
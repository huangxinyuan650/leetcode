# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/12/19 17:13
# File: celery_task_demo.py

from celery import Celery

app = Celery('celery_task_demo')】 把v
app.config_from_object('celery_task_demo_config')


@app.task
def add(x, y):
    return x + y


if __name__ == '__main__':
    app.worker_main()

# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/12/19 17:47
# File: celery_task_demo_config.py
broker_url = 'redis://127.0.0.1:6379/2'
result_backend = 'redis://127.0.0.1:6379/3'

# _*_ coding:utf-8_*_
# Author:   Ace Huang
# Time: 2020/12/19 17:20
# File: celery_task_call.py


if __name__ == '__main__':
    from celery_task_demo import add
    import time

    _r = add.delay(1, 2)
    _wait_count = 0
    while not _r.ready():
        _wait_count += 1
        print(f'{_wait_count}')
        time.sleep(1)

    print(f'Result:{_r.get()}')

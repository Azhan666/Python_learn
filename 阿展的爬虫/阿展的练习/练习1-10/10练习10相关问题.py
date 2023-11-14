# !/usr/bin/env python
# -*- coding: utf-8 -*-

# 创建一个“队列”对象

from queue import Queue
#
# myqueue = queue.Queue(maxsize=10)
# Queue.Queue类即是一个队列的同步实现。队列长度可为无限或者有限。可通过Queue的构造函数的可选参数maxsize来设定队列长度。如果maxsize小于1就表示队列长度无限。
# 将一个值放入队列中
# myqueue.put(10)
# 调用队列对象的put()
# 方法在队尾插入一个项目。put()
# 有两个参数，第一个item为必需的，为插入项目的值；第二个block为可选参数，默认为1。如果队列当前为空且block为1，put()
# 方法就使调用线程暂停, 直到空出一个数据单元。如果block为0，put方法将引发Full异常。
# 将一个值从队列中取出
# myqueue.get()
# 调用队列对象的get()
# 方法从队头删除并返回一个项目。可选参数为block，默认为True。如果队列为空且block为True，get()
# 就使调用线程暂停，直至有项目可用。如果队列为空且block为False，队列将引发Empty异常。
# python
# queue模块有三种队列:
# 1、python
# queue模块的FIFO队列先进先出。
# 2、LIFO类似于堆。即先进后出。
# 3、还有一种是优先级队列级别越低越先出来。
# 针对这三种队列分别有三个构造函数:
# 1、

# class Queue.Queue(maxsize) FIFO
#
#
# # 2、
#
# class Queue.LifoQueue(maxsize) LIFO
#
#
# # 3、
#
# class Queue.PriorityQueue(maxsize) # 优先级队列


# 介绍一下此包中的常用方法:
#
# Queue.qsize()
# 返回队列的大小
# Queue.empty()
# 如果队列为空，返回True, 反之False
# Queue.full()
# 如果队列满了，返回True, 反之False
# Queue.full
# 与
# maxsize
# 大小对应
# Queue.get([block[, timeout]])获取队列，timeout等待时间
# Queue.get_nowait()
# 相当Queue.get(False)
# 非阻塞
# Queue.put(item)
# 写入队列，timeout等待时间
# Queue.put_nowait(item)
# 相当Queue.put(item, False)
# Queue.task_done()
# 在完成一项工作之后，Queue.task_done()
# 函数向任务已经完成的队列发送一个信号
# Queue.join()
# 实际上意味着等到队列为空，再执行别的操作
#
# 附上一个例子:

# coding:utf-8
import queue
import threading
import time
import random

q = Queue.Queue(0)  # 当有多个线程共享一个东西的时候就可以用它了
NUM_WORKERS = 3


class MyThread(threading.Thread):

    def __init__(self, input, worktype):
        self._jobq = input
        self._work_type = worktype
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if self._jobq.qsize() > 0:
                self._process_job(self._jobq.get(), self._work_type)
            else:
                break

    def _process_job(self, job, worktype):
        doJob(job, worktype)


def doJob(job, worktype):
    time.sleep(random.random() * 3)
    print
    "doing", job, " worktype ", worktype


if __name__ == '__main__':
    print
    "begin...."
    # for i inrange(NUM_WORKERS * 2):
    #     q.put(i)  # 放入到任务队列中去
    # print
    # "job qsize:", q.qsize()
    # for x inrange(NUM_WORKERS):
    #     MyThread(q, x).start()

# Queue线程安全队列：
#
# 在线程中，访问一些全局变量，加锁是一个经常的过程。如果你是想把一些数据存储到某个队列中，那么Python内置了一个线程安全的模块叫做queue模块。Python中的queue模块中提供了同步的、线程安全的队列类，包括FIFO（先进先出）队列Queue，LIFO（后入先出）队列LifoQueue。这些队列都实现了锁原语（可以理解为原子操作，即要么不做，要么都做完），能够在多线程中直接使用。可以使用队列来实现线程间的同步。相关的函数如下：
#
# 初始化Queue(maxsize)：创建一个先进先出的队列。
# qsize()：返回队列的大小。
# empty()：判断队列是否为空。
# full()：判断队列是否满了。
# get()：从队列中取最后一个数据。
# put()：将一个数据放到队列中。


# 使用生产者与消费者模式多线程下载表情包：
import threading
import requests
from lxml import html
etree = html.etree
from urllib import request
import os
import re
from queue import Queue


class Producer(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Producer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            self.parse_page(url)

    def parse_page(self, url):
        response = requests.get(url, headers=self.headers)
        text = response.text
        html = etree.HTML(text)
        imgs = html.xpath("//div[@class='page-content text-center']//a//img")
        for img in imgs:
            if img.get('class') == 'gif':
                continue
            img_url = img.xpath(".//@data-original")[0]
            suffix = os.path.splitext(img_url)[1]
            alt = img.xpath(".//@alt")[0]
            alt = re.sub(r'[，。？?,/\\·]', '', alt)
            img_name = alt + suffix
            self.img_queue.put((img_url, img_name))


class Consumer(threading.Thread):
    def __init__(self, page_queue, img_queue, *args, **kwargs):
        super(Consumer, self).__init__(*args, **kwargs)
        self.page_queue = page_queue
        self.img_queue = img_queue

    def run(self):
        while True:
            if self.img_queue.empty():
                if self.page_queue.empty():
                    return
            img = self.img_queue.get(block=True)
            url, filename = img
            request.urlretrieve(url, 'images/' + filename)
            print(filename + '  下载完成！')


def main():
    page_queue = Queue(100)
    img_queue = Queue(500)
    for x in range(1, 101):
        url = "http://www.doutula.com/photo/list/?page=%d" % x
        page_queue.put(url)

    for x in range(5):
        t = Producer(page_queue, img_queue)
        t.start()

    for x in range(5):
        t = Consumer(page_queue, img_queue)
        t.start()


if __name__ == '__main__':
    main()
# GIL全局解释器锁：
#
# Python自带的解释器是CPython。CPython解释器的多线程实际上是一个假的多线程（在多核CPU中，只能利用一核，不能利用多核）。同一时刻只有一个线程在执行，为了保证同一时刻只有一个线程在执行，在CPython解释器中有一个东西叫做GIL（Global
# Intepreter
# Lock），叫做全局解释器锁。这个解释器锁是有必要的。因为CPython解释器的内存管理不是线程安全的。当然除了CPython解释器，还有其他的解释器，有些解释器是没有GIL锁的，见下面：
#
# Jython：用Java实现的Python解释器。不存在GIL锁。更多详情请见：https: // zh.wikipedia.org / wiki / Jython
# IronPython：用.net实现的Python解释器。不存在GIL锁。更多详情请见：https: // zh.wikipedia.org / wiki / IronPython
# PyPy：用Python实现的Python解释器。存在GIL锁。更多详情请见：https: // zh.wikipedia.org / wiki / PyPy
# GIL虽然是一个假的多线程。但是在处理一些IO操作（比如文件读写和网络请求）还是可以在很大程度上提高效率的。在IO操作上建议使用多线程提高效率。在一些CPU计算操作上不建议使用多线程，而建议使用多进程。
# 多线程下载百思不得姐段子作业：
import requests
from lxml import html
etree = html
import threading
from queue import Queue
import csv


class BSSpider(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    def __init__(self, page_queue, joke_queue, *args, **kwargs):
        super(BSSpider, self).__init__(*args, **kwargs)
        self.base_domain = 'http://www.budejie.com'
        self.page_queue = page_queue
        self.joke_queue = joke_queue

    def run(self):
        while True:
            if self.page_queue.empty():
                break
            url = self.page_queue.get()
            response = requests.get(url, headers=self.headers)
            text = response.text
            html = etree.HTML(text)
            descs = html.xpath("//div[@class='j-r-list-c-desc']")
            for desc in descs:
                jokes = desc.xpath(".//text()")
                joke = "\n".join(jokes).strip()
                link = self.base_domain + desc.xpath(".//a/@href")[0]
                self.joke_queue.put((joke, link))
            print('=' * 30 + "第%s页下载完成！" % url.split('/')[-1] + "=" * 30)


class BSWriter(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
    }

    def __init__(self, joke_queue, writer, gLock, *args, **kwargs):
        super(BSWriter, self).__init__(*args, **kwargs)
        self.joke_queue = joke_queue
        self.writer = writer
        self.lock = gLock

    def run(self):
        while True:
            try:
                joke_info = self.joke_queue.get(timeout=40)
                joke, link = joke_info
                self.lock.acquire()
                self.writer.writerow((joke, link))
                self.lock.release()
                print('保存一条')
            except:
                break


def main():
    page_queue = Queue(10)
    joke_queue = Queue(500)
    gLock = threading.Lock()
    fp = open('bsbdj.csv', 'a', newline='', encoding='utf-8')
    writer = csv.writer(fp)
    writer.writerow(('content', 'link'))

    for x in range(1, 11):
        url = 'http://www.budejie.com/text/%d' % x
        page_queue.put(url)

    for x in range(5):
        t = BSSpider(page_queue, joke_queue)
        t.start()

    for x in range(5):
        t = BSWriter(joke_queue, writer, gLock)
        t.start()


if __name__ == '__main__':
    main()

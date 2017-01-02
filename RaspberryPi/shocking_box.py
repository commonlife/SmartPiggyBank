#-*- coding: utf-8 -*-
""" python 2.7 """

import RPi.GPIO as GPIO
import time

import urllib

class NetworkTool:
    def __init__(self):
        self.request_url = "http://114.202.246.130/hack2016/api/money/save"

    def request_for_get(self, total_money, value_of_500, value_of_100):
        # http://10.203.206.45:5000/api/money/save?money=80000&id=default&500=100&100=300
        request_url = "{}?id=default&money={}&500={}&100={}".format(self.request_url, total_money, value_of_500, value_of_100)
        data = urllib.urlopen(request_url).read()
        print(data)

    def request_for_post(self, count_of_500, count_of_100):
        total_money = (count_of_500*500) + (count_of_100*100)
        params = urllib.urlencode({
            'id': 'default',
            'money': total_money,
            '500': count_of_500,
            '100': count_of_100
        })

        data = urllib.urlopen(self.request_url, params).read()
        print(data)

input_pin_num_for_500 = 18 # GPIO18
input_pin_num_for_100 = 23 # GPIO23
GPIO.setmode(GPIO.BCM)
GPIO.setup(input_pin_num_for_500, GPIO.IN)
GPIO.setup(input_pin_num_for_100, GPIO.IN)

def request_info():
    networkTool = NetworkTool()
    f_500 = open('./money_500.txt', 'r')
    saved_money_500 = int(f_500.read())
    f_500.close()
    f_100 = open('./money_100.txt', 'r')
    saved_money_100 = int(f_100.read())
    f_100.close()
    total_money = (saved_money_500*500) + (saved_money_100*100)
    networkTool.request_for_get(total_money, saved_money_500, saved_money_100)

def write_500_won():
    saved_money = 0
    try:
        f = open('./money_500.txt', 'r')
        saved_money = int(f.read())
        f.close()
    except IOError:
        pass
    now_money = 0
    if saved_money == None:
        pass
    else:
        now_money = int(saved_money) + 1
    f = open('./money_500.txt', 'w')
    f.write(str(now_money))
    f.close()
    request_info()

def write_100_won():
    saved_money = 0
    try:
        f = open('./money_100.txt', 'r')
        saved_money = int(f.read())
        f.close()
    except IOError:
        pass

    now_money = 0
    if saved_money == None:
        pass
    else:
        now_money = int(saved_money) + 1
    f = open('./money_100.txt', 'w')
    f.write(str(now_money))
    f.close()
    request_info()

# write_500_won()
# write_100_won()

try:
    request_info()
    while True:
        # 1 == No Input , 0 == something is passed
        value_for_500 = GPIO.input(input_pin_num_for_500)
        value_for_100 = GPIO.input(input_pin_num_for_100)
        if value_for_500 == 0:
            # 500 won passed
            write_500_won()
            time.sleep(1)
        elif value_for_100 == 0:
            # 100 won passed
            write_100_won()
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()

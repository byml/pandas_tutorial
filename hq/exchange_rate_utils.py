# -*- coding: utf-8 -*-
import requests
import time

def get_exchange_rate(orignal_currency = 'hkd', target_currency = 'cny'):
    now = int(round(time.time() * 1000))
    orignal_currency = orignal_currency.lower()
    target_currency = target_currency.lower()
    url = 'https://hq.sinajs.cn/rn=%ilist=fx_s%s%s' % (now,orignal_currency,target_currency)
    response = requests.get(url)
    exchange_rate = response.text.split(',')[1]
    return exchange_rate
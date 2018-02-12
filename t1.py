# -*- coding: utf-8 -*-

import requests

from hq import exchange_rate_utils as exu

print(exu.get_exchange_rate())
print(exu.get_exchange_rate('USD'))

response = requests.get('http://int-loms-rws.optilink.com:8132/orders/show?id=1&carrier_id=1')
print(response.json()['order_detail']['order']['company_name'])
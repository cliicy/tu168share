# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import re
import sys
import time
sys.path.append('../mycrawler')

match=re.search( r"(\d+\.?\d*)","aa123,4,567,89,3.456".replace(",",""))
print(match.group())
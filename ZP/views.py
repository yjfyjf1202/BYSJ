import json
import time

import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Create your views here
from django.views.decorators.http import require_http_methods
from lxml import etree
from LOGIN import models

headers_dict = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/86.0.4240.75 Safari/537.36 "

}

@require_http_methods(['GET'])
def getZP(request):
    k = []
    url = "https://www.zhipin.cn/jobs/jobs-list.php?sort=&page=1&key=&jobcategory=&education=&citycategory=&experience=&settr=&trade=&wage=&nature="
    res = requests.get(url, headers=headers_dict)
    sele = etree.HTML(res.text)
    job = sele.xpath('//div[@class="p_top"]/a/h2/text()')
    print(job)
    return HttpResponse(k)

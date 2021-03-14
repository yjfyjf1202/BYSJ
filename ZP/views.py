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
    page=request.GET.get("page",default=1)
    url = "https://www.zhipin.cn/jobs/jobs-list.php?sort=&page="+str(page)+"&key=&jobcategory=&education=&citycategory=&experience=&settr=&trade=&wage=&nature="
    res = requests.get(url, headers=headers_dict)
    response=parseData(res)

    return HttpResponse(json.dumps(response))

def parseData(res):
    sele = etree.HTML(res.text)
    job = sele.xpath('//div[@class="p_top"]/a/h2/text()')
    job_zhiding= sele.xpath('//div[@class="p_top"]/a/h2/span/text()')
    if len(job_zhiding)!=0:
        print(type(job))
        job.insert(0,job_zhiding[0])
    corps = sele.xpath('//div[@class="position"]/div[@class="p_bot"]/span/a/text()')
    city = sele.xpath('//div[@class="position"]/div[@class="p_bot"]/div[@class="li_b_l"]/text()')
    salary = sele.xpath('//div[@class="list_item_bot"]/div/span/text()')
    job_url=sele.xpath('//div[@class="p_top"]/a/@href')
    # time=sele.xpath('//div[@class="p_top"]/span/span/text()')
    # print(job_url)
    print(job_zhiding)
    result = dataFilter(salary)
    response = []
    for i in range(len(job)):
        dict_res = {"job": job[i], "corps": corps[i], "city": city[i], "salary": result[i],"job_url":job_url[i]}
        response.append(dict_res)
    return response



def dataFilter(data):
    s = ""
    j = 0
    res = []
    for i in range(len(data)):
        if i % 3 == 0 and i != 0:
            res.append(s)
            s = ""
            s = s + data[i]+" "
            # print("这是一号标记位",i,s)
        else:

            s = s + data[i]+" "
            # print("这是二号号标记位",i, s)
    # print(s)
    res.append(s)
    # for j in range(len(res)):
    #     print(j,res[j])
    return res

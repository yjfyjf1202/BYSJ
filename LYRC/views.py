from django.shortcuts import render

# Create your views here.
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
def getLYRCJob(request):
    page = request.GET.get('page', default="1")
    lv=request.GET.get('lv',default="")
    p = page
    # print(p)
    url = "http://www.hrm.cn/jobs?keyType=0&keyWord=&jobTypeId=&jobType=&industry=&industryname=&workId=&workPlace=&salary="+lv+"&entType=&experience=&education=&entSize=&benefits=&reftime=&workTypeId=&sortField=&pageNo=" + str(
        p)
    # print("一号标记位",url)
    res=getResponse(url)
    return HttpResponse(json.dumps(res))

def getResponse(url):
    res = requests.get(url=url, headers=headers_dict)
    # 将获得的html内容转换成标准的HTML
    sele = etree.HTML(res.text)
    # 提取岗位名称
    position = sele.xpath("//span[@class='jobs_name_list_name']/text()")
    # 提取招聘单位
    corps = sele.xpath("//li[@class='list_com_name']/a/text()")
    # 提取薪酬
    salarys = sele.xpath("//div[@class='list_jobs_box list clearfix']/ul/li[@class='list_jobs_salary']/text()")
    salary = []
    # 提取工作地点
    location = sele.xpath("//div[@class='list_jobs_box list clearfix']/ul/li[@class='list_jobs_city']/text()")
    # 提取发布时间
    time = sele.xpath("//div[@class='list_jobs_box list clearfix']/ul/li[@class='list_jobs_date']/text()")
    # 获取链接
    htm = sele.xpath("//a[@class='jobs_name_list']/@href")
    salary_url = sele.xpath('//ul[@id="salary_cur"]/li/a/text()')
    salary_lv = sele.xpath('//ul[@id="salary_cur"]/li/a/@lv')
    # print(salary_url)
    # print(res.text)
    # print(salary_lv)
    # salary_lv[0] = "0"
    res_lv = []
    for l in range(len(salary_url)):
        # if salary_lv[l] == '':
        #     salary_lv[l] = "0"
        dict_lv = {"salary_url": salary_url[l], "salary_lv": salary_lv[l]}
        res_lv.append(dict_lv)
    # res_lv={"salary_url": salary_url, "salary_lv": salary_lv}

    for k in range(len(htm)):
        htm[k] = "http://www.hrm.cn" + htm[k]

    for i in range(0, len(position)):
        if (len(position) == 0):
            continue
        else:
            xs = salarys[i]
            xs1 = xs.strip()
            xse = xs1.replace(" ", "")
            xse1 = xse.replace("\r", "")
            xse2 = xse1.replace("\n", "")
            salary.append(xse2)

    res = []

    dict_salv = {"res_lv": res_lv}
    for j in range(len(position)):
        dict_all = {"job": position[j], 'corps': corps[j], "salary": salary[j], "location": location[j],
                    "time": time[j], "url": htm[j], }
        res.append(dict_all)

    res.append(dict_salv)
    return res


def screenInfo(request):
    lv=request.GET.get("lv",default="")
    url="http://www.hrm.cn/jobs?keyType=0&keyWord=&jobTypeId=&jobType=&industry=&industryname=&workId=&workPlace=&salary="+lv+"&entType=&experience=&education=&entSize=&benefits=&reftime=&workTypeId=&sortField=&pageNo=1"
    print("二号标记位", url)
    res=getResponse(url)
    print(lv)
    return HttpResponse(json.dumps(res))



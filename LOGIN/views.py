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
def getJobList(request):
    page = request.GET.get('page', default="p1")
    # print(page)
    url = "https://jobs.51job.com/" + page
    res = parseQCWY(url)

    return HttpResponse(json.dumps(res))


def parseQCWY(url):
    try:
        # print("这是标记1", url)
        select = requests.get(url=url, headers=headers_dict)
        select.encoding = 'GBK'
        response = etree.HTML(select.text)

        job = response.xpath('//div[@class="e "]/p/span/a/text()')
        job_last = response.xpath('//div[@class="e ebtm"]/p/span/a/text()')
        job.append(job_last)
        # 公司
        corp = response.xpath('//div[@class="e "]/p/a[@class="name"]/text()')
        corp_last = response.xpath('//div[@class="e ebtm"]/p/a[@class="name"]/text()')
        corp.append(corp_last)
        # 地点
        location = response.xpath('//div[@class="e "]/p/span[@class="location name"]/text()')
        location_last = response.xpath('//div[@class="e ebtm"]/p/span[@class="location name"]/text()')
        location.append(location_last)
        time = response.xpath('//div[@class="e "]/p/span[@class="time"]/text()')
        time_last = response.xpath('//div[@class="e ebtm"]/p/span[@class="time"]/text()')
        time.append(time_last)
        # 要求
        order = response.xpath('//div[@class="e "]/p[@class="order"]/text()')
        order_last = response.xpath('//div[@class="e ebtm"]/p[@class="order"]/text()')
        for l in order_last:
            order.append(l)
        # print(len(order))
        # 岗位介绍
        introduction = response.xpath('//div[@class="e "]/p[@class="text"]/text()')
        introduction_last = response.xpath('//div[@class="e ebtm"]/p[@class="text"]/text()')
        introduction.append(introduction_last)
        list = []
        # 把order里的字符每四个为一组整理好
        # 整理好
        j = 0
        s = ""
        for i in range(len(order)):
            if i % 4 == 0 and i != 0 or i == 79:
                j = j + 1
                list.append(s)
                # print(i,s)
                s = ""
                s = s + order[i] + " "

            else:
                # print(i,s)
                s = s + order[i] + " "
        # print(len(list))
        res = []

        # print(list)
        # print(list,len(list))
        for i in range(len(job)):
            dist = {"job": job[i], "corp": corp[i], "location": location[i], "time": time[i], "order": list[i],
                    "introduction": introduction[i]}

            res.append(dist)
        return res
    except Exception as e:
        pass
        # print(len(job), len(corp), len(location), len(time), len(list), len(introduction))


def qcwyScreen(request):
    res_hy = models.HyKeyWd.objects.all()
    res_xc = models.XcKeyWd.objects.all()
    res_ed = models.EdKeyWd.objects.all()
    res_we = models.WeKeyWd.objects.all()
    res_rt = models.RtKeyWd.objects.all()
    res_yx = models.QCWYInfo.objects.all()
    res_wt = models.WtKeyWd.objects.all()
    res_zy = models.ZyKeyWd.objects.all()
    r_hy = ScreenDatafilter(res_hy)
    r_xc = ScreenDatafilter(res_xc)
    r_ed = ScreenDatafilter(res_ed)
    r_we = ScreenDatafilter(res_we)
    r_rt = ScreenDatafilter(res_rt)
    r_yx = ScreenDatafilter(res_yx)
    r_wt = ScreenDatafilter(res_wt)
    r_zy = ScreenDatafilter(res_zy)
    print(r_hy)
    response = {'r_hy': r_hy, 'r_xc': r_xc, 'r_ed': r_ed, 'r_we': r_we, 'r_rt': r_rt, 'r_yx': r_yx, 'r_wt': r_wt,
                'r_zy': r_zy}
    return HttpResponse(json.dumps(response))


def ScreenDatafilter(res):
    url = []
    key = []
    response = []
    i = 0
    for e in res:
        url.append(e.url)
        key.append(e.keywd)
        result = {"url": url[i], "key": key[i]}
        i = i + 1
        response.append(result)
    return response


def ScreenQCWYData(request):
    hy = request.GET.get('hy', default=None)
    yx = request.GET.get('yx', default=None)
    we = request.GET.get('we', default=None)
    rt = request.GET.get('rt', default=None)
    wt = request.GET.get('wt', default=None)
    zy = request.GET.get('zy', default=None)
    ed = request.GET.get('ed', default=None)
    page = request.GET.get('page', default='p1')
    p = str(page)
    b = p.find("p")
    if b == -1:
        page = "p" + p
    # print(b)
    print(hy, yx, we, rt, wt, zy, ed, page)
    gengduo = [hy, yx, we, rt, wt, ed, zy]
    print(gengduo)
    url = addUrl(gengduo, page)
    # print(url)
    res = parseQCWY(url)
    return HttpResponse(json.dumps(res))


def addUrl(data, page):
    url = "https://jobs.51job.com/"
    t = "https://jobs.51job.com/"
    print(type(page))
    if data[0] != '' or data[1] != '' or data[2] != '' or data[3] != '' or data[4] != '' or data[5] != '' or data[
        6] != '':

        if data[6] != '':
            t = url = url + data[6] + "/"
            # print(url)
            for i in range(len(data)):
                if data[i] == '' or i == 6:
                    continue
                elif data[i] != '':
                    print(i)
                    url = url + data[i] + "_"
                else:
                    url = url + data[i]

        else:
            for i in range(len(data)):
                if data[i] is None:
                    continue
                elif i >= 1 and t != url and data[i] is None:
                    url = url + "_" + data[i]
                else:
                    url = url + data[i]
        url = url + "/" + page
        print("这是二号标记位", url)
    else:
        url = "https://jobs.51job.com/" + page
    return url


def SeacherQCWY(request):
    keyword = "%25e5%2590%258e%25e7%25ab%25af"
    page1 = 1
    j = 0
    response = {}
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99," + keyword + ",2," + str(
        page1) + ".html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare="

    res = requests.get(url, headers=headers_dict)
    res = requests.get(url, headers=headers_dict)
    res.encoding = "gbk"
    selet = etree.HTML(res.text)
    data = selet.xpath('//script/text()')
    # a=json.dumps(data[4])
    a = data[4]
    b = a.replace("\r", "")
    c = b.replace("\n", "")

    d = "window.__SEARCH_RESULT__ = "
    e = c.replace(d, '')
    f = eval(e)
    print(type(f['engine_search_result']))
    for i in f['engine_search_result']:
        print(i['job_name'])
        print("*" * 30)

    # d=json.loads(c)
    # print(d)
    # d=json.dumps(c)

    return HttpResponse(f)





@require_http_methods(['GET'])
def insertQCWY(request):
    pass



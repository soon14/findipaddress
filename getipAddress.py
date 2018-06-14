# -*- coding: UTF-8 -*-
import os
import geoip2.database
#如果不使用 #使用中文国家名显示下面就可以注释掉
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

def getIp(ip):

    # 读取Geo city库s
    #print (sys.path)
    #print (os.path.join(BASE_DIR))
    reader = geoip2.database.Reader(r'GeoLite2-City.mmdb')
    # 查询国家及城市
    try:
        response = reader.city(ip)
        #这里要注意,如果使用中文须要import一下sys并setdefaultencoding
        gj = str(response.country.names['zh-CN'])
        cs = str(response.city.name)
        gjcs = gj + ',' + cs
        #print(gjcs)

        return gjcs

    except:
        pass
#getIp('192.168.1.200')

def getIpxy(ip):

    # 读取Geo city库s
    #print (sys.path)
    #print (os.path.join(BASE_DIR))
    reader = geoip2.database.Reader(r'GeoLite2-City.mmdb')
    # 查询xy
    try:
        response = reader.city(ip)
        #经度及纬度
        s_jing = str(response.location.longitude)
        s_wei = str(response.location.latitude)
        #合并经纬度
        s_jing_wei = s_jing + "," + s_wei
        return s_jing_wei
        #print(s_jing_wei)

    except:
        pass
#getIpxy('254.25.254.254')
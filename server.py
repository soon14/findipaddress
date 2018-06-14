# coding:utf-8

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options
import os
import datetime
import config
from getipAddress import getIp,getIpxy
import re

from tornado.web import RequestHandler
from tornado.options import define, options
from tornado.websocket import WebSocketHandler
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='logs/log.log',
                    filemode='a')

#################################################################################################
# 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)


#################################################################################################


define("port", default=8000, type=int)
define("host", default='127.0.0.1')

class IndexHandler(RequestHandler):

    def get(self):

        self.encoding = 'utf-8'
        # 获取远程客户端IP做为默认值
        ip = self.request.remote_ip
	logging.debug("access IP")
	logging.debug(ip)
        # 使用getipAddress模块中的getIpxy
        fip = getIp(ip)
        fipxy = getIpxy(ip)
        fipxy = unicode(fipxy)
        # 如果远端IP为空,额,这情况一般不会出现,但是真的为空了,那么就给一个初始默认值,否则切片会出错
        if fipxy == "None":
            fx = "0"
            fy = "0"
        else:
            fxy = fipxy.split(',')
            fx = fxy[0]
            fy = fxy[1]
        # 接收表单数据
        if 'q' in self.request.arguments:
            ip = self.get_argument('q')

            # 判断是否为一个IP地址
            p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
            if p.match(ip):
                fip = getIp(ip)
                fipxy = getIpxy(ip)
                # 判断输入的IP是否为保留(如果保留的话会出现空值,在空值的情况下会split会报错)
                if fipxy is None:

                    ip = "保留地址."
                    self.render('findip_error.html',ip=ip)
                else:
                    fxy = fipxy.split(',')
                    fx = fxy[0]
                    fy = fxy[1]
                    self.render('findip.html', ip=ip ,fx=fx ,fy=fy ,fip=fip)

            else:
                if ip == "":

                    ipnone = "输入了空的IP地址."
                    self.render('findip_error.html', ip=ipnone)
                else:

                    isnotip = ip
                    self.render('findip_error.html', ip=isnotip)

        else:

            self.render('findip.html', ip=ip ,fx=fx ,fy=fy ,fip=fip)

    post = get



if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application([
            (r"/", IndexHandler),

        ],
        #这里是直接写死配置路径
        #static_path = os.path.join(os.path.dirname(__file__), "static"),
        #template_path = os.path.join(os.path.dirname(__file__), "template"),
        #这里是从配置文件 config.py中引入配置
        **config.settings
        )
    http_server = tornado.httpserver.HTTPServer(app)
    #http_server.listen(options.port)
    #tornado.ioloop.IOLoop.current().start()
    http_server.bind(options.port)
    http_server.start(num_processes=0)#0按CPU核心,1开启两个,2为三个
    tornado.ioloop.IOLoop.instance().start()


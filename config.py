# coding:utf-8
import os

redis_options = {
    'redis_host':'127.0.0.1',
    'redis_port':6379,
    'redis_pass':'',
}

settings = {
    'template_path': os.path.join(os.path.dirname(__file__), 'template'),
    'static_path': os.path.join(os.path.dirname(__file__), 'static'),
    'cookie_secret':'0Q1AKOKTQHqaa+N80XhYW7KCGskOUE2snCW06UIxXgI=',
    'xsrf_cookies':False,
    'login_url':'/login',
    'debug':False,
}

log_path = os.path.join(os.path.dirname(__file__), 'logs/log')


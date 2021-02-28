import os

port = os.environ['PORT']

bind = "0.0.0.0:{}".format(port)
workers = 2
threads = 2
timeouts = 120
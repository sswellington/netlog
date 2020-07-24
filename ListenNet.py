import json
import speedtest

class ListenNet(object):
    listen = None

    def __init__(self):
        self.listen = speedtest.Speedtest() # line 1073
    
    def info(self):
        self.listen.get_servers([])
        self.listen.get_best_server()
        # in bit
        self.listen.download() 
        self.listen.upload()
        """ return {
            'download': self.listen.results.download,
            'upload': self.listen.results.upload,
            'ping': self.listen.results.ping,
            'server': self.listen.results.server,
            'timestamp': self.listen.results.timestamp,
            'bytes_sent': self.listen.results.bytes_sent,
            'bytes_received': self.listen.results.bytes_received,
            'share': self.listen.results._share,
            'client': self.listen.results.client,
        } """
        return (self.listen.results.dict)

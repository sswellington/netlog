import json
import speedtest


class ListenNet(object):
    info: None
    ping: float
    upload: float
    download: float
    listen = speedtest.Speedtest() 

    def __init__(self, set_server=[]):
        """ Arrumar a interface """


        self.listen = speedtest.Speedtest()  # line 1073
        print("Testing from Y")
        print("Connect Server.............................")
        self.listen.get_servers(set_server)
        print("Selecting best server based on ping........")
        self.listen.get_best_server()
        # print("Hosted by ", (hosted['Sponsor']))
        self.ping = self.listen.results.ping
        """ in bit """
        self.download = self.listen.download()
        self.upload = self.listen.upload()
        """ info
            Return dictionary of result data {
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
        self.info = self.listen.results.dict()

    def get_url(self):
        """POST data to the speedtest.net API to obtain a share results link"""
        return self.listen.results.share()

    def report(self):
        """ Doc: Use the lib `json` - RFC 7159
		    [Source](https://docs.python.org/3/library/json.html?highlight=json#module-json)
        """
        json_object = json.dumps(self.info, indent = 4) 
        with open("report.json", "w") as outfile: 
            outfile.write(json_object) 
import json
import speedtest

class ListenNet(object):
    """ listen = speedtest
        ...
        Run: 
            speedtest-cli
            speedtest-cli --simple
            speedtest-cli --share
        ...
        font: 
            https://pypi.org/project/speedtest-cli/
            https://github.com/sivel/speedtest-cli/wiki
            https://www.geeksforgeeks.org/test-internet-speed-using-python/
            https://stackoverflow.com/questions/41716064/how-do-i-use-speedtest-cli-or-any-alternative-in-python-script-instead-of-comman
    """
    listen = None

    def __init__(self):
        self.listen = speedtest.Speedtest() # line 1073

    def set_servers(self, server):
        self.servers(server)
    def get_servers(self):
        return self.servers

    def get_internet_test(self):
        """ -> Refactor
            verificar o motivo que os métodos não acessam: 
                - uns aos outros os atributos.
                - os atributos
        """        
        self.servers()
        self.best_server()
        self.upload()
        self.download()

    def servers(self):
        servers = [] # If you want to test against a specific server
        self.listen.get_servers(servers)

    def best_server(self):
        self.listen.get_best_server()

    def upload(self):
        # add feature: convert to megabytes 
        return self.listen.upload(threads=None)

    def download(self):
        # add feature: convert to megabytes 
        # If you want to use a single threaded test
        return self.listen.download(threads=None)

    def share(self):
        self.get_internet_test()
        return self.listen.results.share()

    def export(self):
        self.get_internet_test()
        """ Doc: Use the lib `json` - RFC 7159
		https://docs.python.org/3/library/json.html?highlight=json#module-json	
        """
        json_object = json.dumps((self.listen.results.dict()), indent = 4) 
        with open("netlog.json", "w") as outfile: 
            outfile.write(json_object) 

    def __done__(self):  
        pass 

if __name__ == '__main__':
    print("begin") # development variable
    try:
        t = ListenNet()
        print(t.share())
    except Error:
        print("Error 23: ListenNet")
print("end") # development variable
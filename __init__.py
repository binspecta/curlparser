import re
import json

class curlparser():
    url = None
    headers = {}
    data = None
    json_data = None

    def print_all(self):
        print self.headers
        print self.data

    def parse(self, s):
        ## parse url
        re_set = re.findall("curl '(.*?)'", s)
        self.url = re_set[0]
        
        ## parse headers
        re_set = re.findall("-H '(.*?)'", s)
        # print re_set
        # print len(re_set)

        for r in re_set:
            t = r.split(': ')
            self.headers[t[0]] = t[1]

        ## parse data
        re_set = re.findall("--data-binary '(.*?)'", s)
        self.data = re_set[0]

        return {
            'url': self.url,
            'headers': self.headers,
            'data': self.data,
        }

    def beautify(self):
        self.json_data = json.loads(self.data)
        s = json.dumps(self.json_data, indent=4)
        print s

    def b(self, s):
        j = json.loads(s)
        s = json.dumps(j, indent=4)
        print s
        
if __name__ == '__main__':
    ex = '''curl 'github.com''''

    p = curlparser()
    p.parse(ex)
    p.print_all()

    print p.headers
    print p.data


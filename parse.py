import re

class curlparser():
    headers = {}
    data = {}

    def print_all(self):
        print self.headers
        print self.data

    def parse(self, s):
        # parse headers
        re_set = re.findall("-H '(.*?)'", s)
        # print re_set
        # print len(re_set)

        for r in re_set:
            t = r.split(': ')
            self.headers[t[0]] = t[1]

        re_set = re.findall("--data-binary '(.*?)'", s)
        self.data = re_set[0]
        

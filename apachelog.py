#!/root/nsd1905/bin/python3
import re
import collections
class CountPatt:
    
    def __init__(self,patt):
        self.cpatt = re.compile(patt)
    
    def count_patt(self,fname):
        
        counter = collections.Counter()
       
        with open(fname) as fobj:
       
            for line in fobj:
       
                m = self.cpatt.search(line)
        
                if m:
        
                    counter.update([m.group()])
    
        return counter
if __name__ == "__main__":
    fname = "access_log.txt"
    ip_patt = "^(\d+\.){3}\d+"
    br_patt = "Firefox|MSIE|Chrome"
    ip = CountPatt(ip_patt)
    print(ip.count_patt(fname))
    br = CountPatt(br_patt)
    print(br.count_patt(fname))

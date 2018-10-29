import numpy as np
import csv
#import matplotlib.pyplot as plt

import urllib.request
 
headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
 
req = urllib.request.Request('http://ftp.cs.wisc.edu/math-prog/cpo-dataset/machine-learn/cancer/WDBC/WDBC.dat', headers = headers)
html = urllib.request.urlopen(req).read()
print(html)

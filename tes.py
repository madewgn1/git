import os, time
from os import *
def index():
    #return 'git clone ' + request.url + 'repo-name'
    pat = "repos"
    repo = os.listdir(pat)
    b = []
    for i in repo:
        ti_c = os.path.getmtime(pat + "/" + i)
        c = time.ctime(ti_c)
        b.append(c)
    print(b)
index()

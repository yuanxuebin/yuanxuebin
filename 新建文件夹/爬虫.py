import re
import urllib.request
r=urllib.request.urlopen("http://118.31.19.120:3000/")
html = r.read().decode('utf-8')
print(html)



html =  '''<span class="top_score">7315</span>
           <span class="top_score">7316</span>
           <span class="top_score">7317</span>
           <span class="top_score">7318</span>
           <span class="top_score">7319</span>'''
res = re.findall('<span class="top_score">(.+?)</span>',html)
print(res)
import json
d=json.load(open('data.json',encoding='utf-8'))
s=json.dumps(d,ensure_ascii=False).replace('</','<\\/')
t=open('index.template.html',encoding='utf-8').read().replace('/*__SEED__*/',s)
open('index.html','w',encoding='utf-8').write(t)

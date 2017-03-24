#coding:utf-8
#字典 列表字典生成式
#字符串 字符串转换
#文件操作 文件字典转换 用户登录注册 系统
shoplist=['apple','mango','banana','carrot']
#print shoplist.count('apple')
count=0
for i in shoplist:
    if i=='apple':
        count+=1
        print count
#列表去重
a=[1,2,3,4,1,3,5]
print set(a)

#函数去重
def quchong():
    a=['apple','mango','banana','carrot','apple']
    new=[]
    for i in a:
        if not i in new:
            new.append(i)
    return new
print  quchong()

#将主机192.168.1.1-254存入列表
host_list=[]
netip="192.168.1."
for hostip in range(1,254):
    ip=netip+str(hostip)
    host_list.append(ip)
print host_list

#遍历
for index,value in enumerate(shoplist):
    print index,value

#列表生成式
#格式[x for x in 内容] [x for x in 内容 if 条件]

fields=['a','b','c']
data={'a':'abc','b':'bac','c':'cba'}
print [data[x] for x in fields]

a=[]
for i in fields:
    a.append(data[i])
print a

b=[]
for k,v in data.items():
    b.append(v)
print b

print [v for k,v in data.items()]

print ','.join([data[x] for x in fields])

print ','.join('"%s"' % data[x] for x in fields )

#字典 无序
content={'name':'wd','pc':{'age':18,'iphone':'111'},'woniu':[1,2,3]}
print content.keys()
print content.values()
print content.items()
content['test']=111222333
content.pop("test")
content['pc']['age']=20
content['woniu'][0]=444
print content.get("name","dasdasdas")
print content
res=content.get("name","")
if res:
    print "ok"
else:
    print "fail"

print content.has_key("name")

if  "name" in content:
    print "key is exist"
else:
    print "this is key is no exist"

for k,v in content.items():
    print k,v

#字典应用
for k,v in content.items():
    print k+ ":"
    if type(v)==dict:
         for x,y in v.items():
              print x,y
    elif type(v)==list:
        for z in v:
            print z
    else:
          print v


strcontent="who are  you My name  is  fujinzhou and you"
#字符串取代噢空格
print strcontent.split( " ")
dicts={}
arr=strcontent.split( ' ')
for i in arr:
    if i not in dicts:
        dicts[i]=1
    else:
        dicts[i]+=1
print dicts

#因为很多单词出现了一次，一旦k,v反转， 1作为key ，这个key 会被一只覆盖到最后一个
#方案：把出现的数字作为key，所有出现次数一样的单词保存为列表
reslist={}
for k,v in dicts.items():
    reslist.setdefault(v,[])
    reslist[v].append(k)
print reslist

count=0
f=open('count.html','a+')
f.write("<html><table style='border:solid 1px'>")
f.write("<th style='border:solid 1px'>次数</th><th style='border:solid 1px'>单词</th>")
while count < 4:
    key = max(reslist.keys())
    print key
    print "出现了%s次的单词：%s" % (key,reslist[key])
    for word in reslist[key]:
        f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key,word))
    reslist.pop(key)
    count = count +1
f.write("</table></html>")
f.close()

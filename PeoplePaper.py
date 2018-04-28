# encoding=utf-8
# coding = utf-8

import jieba
import sys
import collections
import math
import numpy as np
import matplotlib.pyplot as plt

dic=dict()
path = "F:\\data\\NLP\\PeoplePaper1946-1949\\PeoplePaper1946-1949\\1946\\1946-"
for j in range(5,10):
    if len(str(j)) == 1:
        j = "0" + str(j)
    for i in range(1,32):
        if len(str(i)) == 1:
            i = "0"+str(i)
        path1 = path+str(j)+"-"+str(i)+"\\"
        for m in range(1,40):
            path2 = path1+str(m)+".txt"

            try:
                f = open(path2,'rt',encoding="utf-8")
            except:
                continue
            lines = f.readlines()
            for line in lines:
                ss = jieba.cut(line,cut_all=False)
                for item in ss:
                    if item not in dic.keys():
                        dic.setdefault(item,1)
                    else:
                        dic[item] += 1

kd = collections.OrderedDict(sorted(dic.items(), key=lambda t: t[1],reverse=True))
X = []
Y = []
i = 1
for key, value in kd.items():
    value1 = math.log(value)
    i1 = math.log(i)
    X.append(i1)
    Y.append(value1)
    i += 1

x = np.array(X)
y = np.array(Y)
print(len(y))
plt.xlim(xmax=10,xmin=0)
plt.ylim(ymax=10,ymin=0)
plt.xlabel("log rank")
plt.ylabel("log frequency")
plt.plot(x, y)
plt.show()

import numpy as np
from DFA_scatter_figure import FN_normal,FN_abnormal
import pandas as pd
import matplotlib.pyplot as plt
import math
logFN_normal = []
logFN_abnormal = []
for i in range(0,len(FN_normal)):
    logFN_normal.append(math.log(FN_normal[i],10))
for i in range(0,len(FN_abnormal)):
    logFN_abnormal.append(math.log(FN_abnormal[i],10))

normal = []
abnormal = []
for i in range(0,len(FN_abnormal)):
    if i%8 == 0 :
        normal.append(float(logFN_normal[i])/math.log(4,10))
        abnormal.append(float(logFN_abnormal[i])/math.log(4,10))
    if i%8 == 1:
        normal.append(float(logFN_normal[i]) / math.log(8, 10))
        abnormal.append(float(logFN_abnormal[i]) / math.log(8, 10))
    if i%8 == 2:
        normal.append(float(logFN_normal[i]) / math.log(20, 10))
        abnormal.append(float(logFN_abnormal[i]) / math.log(20, 10))
    if i%8 == 3:
        normal.append(float(logFN_normal[i]) / math.log(50, 10))
        abnormal.append(float(logFN_abnormal[i]) / math.log(50, 10))
    if i%8 == 4:
        normal.append(float(logFN_normal[i]) / math.log(100, 10))
        abnormal.append(float(logFN_abnormal[i]) / math.log(100, 10))
    if i%8 == 5:
        normal.append(float(logFN_normal[i]) / math.log(200, 10))
        abnormal.append(float(logFN_abnormal[i]) / math.log(200, 10))
    if i%8 == 6:
        normal.append(float(logFN_normal[i]) / math.log(500, 10))
        abnormal.append(float(logFN_abnormal[i]) / math.log(500, 10))
    if i%8 == 7:
        normal.append(float(logFN_normal[i]) / math.log(1000, 10))
        abnormal.append(float(logFN_abnormal[i]) / math.log(1000, 10))

print(normal)
print(abnormal)
data = {

'normal': normal,

'abnormal': abnormal,

}



df = pd.DataFrame(data)
df.plot.box(title="正常与非正常情况下DFA指数的分布图")
plt.grid(linestyle="--", alpha=0.3)
plt.show()

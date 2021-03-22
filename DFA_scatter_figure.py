from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
from DFA_signal_figure import *
import math

FN_abnormal = []
FN_normal = []
member_count = [4,8,20,50,100,200,500,1000]
group_name_abnormal = [epilepsy_1,epilepsy_2,epilepsy_3,epilepsy_4,epilepsy_5]
group_name_normal = [normal_1,normal_2,normal_3,normal_4,normal_5]
for i in range(0,len(group_name_abnormal)):
    for j in range(0,len(member_count)):
        temp_1, fitted_value_1, yk_1, fn_1 = process(group_name_abnormal[i], member_count[j])
        FN_abnormal.append(fn_1)
for i in range(0,len(group_name_normal)):
    for j in range(0,len(member_count)):
        temp_1, fitted_value_1, yk_1, fn_1 = process(group_name_normal[i], member_count[j])
        FN_normal.append(fn_1)
dimension_4_abnormal = []
dimension_8_abnormal = []
dimension_20_abnormal = []
dimension_50_abnormal = []
dimension_100_abnormal = []
dimension_200_abnormal = []
dimension_500_abnormal = []
dimension_1000_abnormal = []
dimension_4_normal = []
dimension_8_normal = []
dimension_20_normal = []
dimension_50_normal = []
dimension_100_normal = []
dimension_200_normal = []
dimension_500_normal = []
dimension_1000_normal = []
x = [0,8,16,24,32]
for i in range(0,len(x)):
    dimension_4_abnormal.append(math.log(FN_abnormal[x[i]],10))
    dimension_8_abnormal.append(math.log(FN_abnormal[x[i] + 1],10))
    dimension_20_abnormal.append(math.log(FN_abnormal[x[i] + 2],10))
    dimension_50_abnormal.append(math.log(FN_abnormal[x[i] + 3],10))
    dimension_100_abnormal.append(math.log(FN_abnormal[x[i] + 4],10))
    dimension_200_abnormal.append(math.log(FN_abnormal[x[i] + 5],10))
    dimension_500_abnormal.append(math.log(FN_abnormal[x[i] + 6],10))
    dimension_1000_abnormal.append(math.log(FN_abnormal[x[i] + 7],10))
    dimension_4_normal.append(math.log(FN_normal[x[i]],10))
    dimension_8_normal.append(math.log(FN_normal[x[i] + 1 ],10))
    dimension_20_normal.append(math.log(FN_normal[x[i] + 2 ],10))
    dimension_50_normal.append(math.log(FN_normal[x[i] + 3 ],10))
    dimension_100_normal.append(math.log(FN_normal[x[i] + 4 ],10))
    dimension_200_normal.append(math.log(FN_normal[x[i] + 5 ],10))
    dimension_500_normal.append(math.log(FN_normal[x[i] + 6 ],10))
    dimension_1000_normal.append(math.log(FN_normal[x[i] + 7 ],10))
log_x = []
for i in range(len(member_count)):
    log_x.append(math.log(member_count[i],10))

x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
for i in range(0,5):
    x1.append(math.log(4, 10))
    x2.append(math.log(8,10))
    x3.append(math.log(20, 10))
    x4.append(math.log(50, 10))
    x5.append(math.log(100, 10))
    x6.append(math.log(200, 10))
    x7.append(math.log(500, 10))
    x8.append(math.log(1000, 10))


plt.scatter(x1, dimension_4_abnormal, marker = 'x',color = 'red', s = 20 ,label = 'First')
plt.scatter(x2, dimension_8_abnormal, marker = 'x',color = 'red', s = 20 ,label = 'First')
plt.scatter(x3, dimension_20_abnormal, marker = 'x',color = 'red', s = 20 ,label = 'First')
plt.scatter(x4, dimension_50_abnormal, marker = 'x',color = 'red', s = 20 ,label = 'First')
plt.scatter(x5, dimension_100_abnormal, marker = 'x',color = 'red', s = 20 ,label = 'First')
plt.scatter(x6, dimension_200_abnormal, marker = 'x',color = 'red', s = 20 ,label = 'First')
plt.scatter(x7, dimension_500_abnormal, marker = 'x',color = 'red', s = 20 ,label = 'First')
plt.scatter(x8, dimension_1000_abnormal, marker = 'x',color = 'red', s = 20 ,label = 'First')
plt.scatter(x1, dimension_4_normal, marker = 'o',color = 'blue', s = 20 ,label = 'First')
plt.scatter(x2, dimension_8_normal, marker = 'o',color = 'blue', s = 20 ,label = 'First')
plt.scatter(x3, dimension_20_normal, marker = 'o',color = 'blue', s = 20 ,label = 'First')
plt.scatter(x4, dimension_50_normal, marker = 'o',color = 'blue', s = 20 ,label = 'First')
plt.scatter(x5, dimension_100_normal, marker = 'o',color = 'blue', s = 20 ,label = 'First')
plt.scatter(x6, dimension_200_normal, marker = 'o',color = 'blue', s = 20 ,label = 'First')
plt.scatter(x7, dimension_500_normal, marker = 'o',color = 'blue', s = 20 ,label = 'First')
plt.scatter(x8, dimension_1000_normal, marker = 'o',color = 'blue', s = 20 ,label = 'First')
plt.title('正常和癫痫的脑电FN值的分布散点图')
plt.show()

# plt.plot(epilepsy_1, label='abnormal_1 plot')
# plt.plot(epilepsy_2, label='abnormal_2 plot')
# plt.plot(normal_1, label='normal plot')
# # generate a legend box
# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0,ncol=3, mode="expand", borderaxespad=0.)
# # annotate an important value
# plt.annotate("Important value", (55, 20), xycoords='data',xytext=(5, 38),arrowprops=dict(arrowstyle='->'))
# plt.show()
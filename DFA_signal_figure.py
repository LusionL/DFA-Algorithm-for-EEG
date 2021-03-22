from open_file import open_file
from matplotlib import pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
from data_process import *
import math
fn = []
epilepsy_1 = open_file('E:/DFA/DFA_DATA/癫痫异常脑电图/20121030105258.txt')
epilepsy_2 = open_file('E:/DFA/DFA_DATA/癫痫异常脑电图/20121031103719.txt')
epilepsy_3 = open_file('E:/DFA/DFA_DATA/癫痫异常脑电图/20121031111404.txt')
epilepsy_4 = open_file('E:/DFA/DFA_DATA/癫痫异常脑电图/20121031113934.txt')
epilepsy_5 = open_file('E:/DFA/DFA_DATA/癫痫异常脑电图/20121031163308.txt')
normal_1 = open_file('E:/DFA/DFA_DATA/正常脑电图/20121030084615.txt')
normal_2 = open_file('E:/DFA/DFA_DATA/正常脑电图/20121030091121.txt')
normal_3 = open_file('E:/DFA/DFA_DATA/正常脑电图/20121030103952.txt')
normal_4 = open_file('E:/DFA/DFA_DATA/正常脑电图/20121030110908.txt')
normal_5 = open_file('E:/DFA/DFA_DATA/正常脑电图/20121030151450.txt')

# plt.plot(epilepsy_1, label='abnormal_1 plot')
# plt.plot(epilepsy_2, label='abnormal_2 plot')
# plt.plot(normal_1, label='normal plot')
# # generate a legend box
# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=0,ncol=3, mode="expand", borderaxespad=0.)
# plt.show()
#
#
#
# temp_1,fitted_value_1,yk_1,fn_1 = process(epilepsy_1,4)
# plt.plot(temp_1,epilepsy_1,'g',temp_1,yk_1,'b',temp_1,fitted_value_1,'r--')
# plt.title('去趋势之后的癫痫脑电信号图Ⅰ(n=4)')
# plt.show()
# fn.append(fn_1)
# temp_1,fitted_value_1,yk_1,fn_1 = process(epilepsy_1,8)
# plt.plot(temp_1,epilepsy_1,'g',temp_1,yk_1,'b',temp_1,fitted_value_1,'r--')
# plt.title('去趋势之后的癫痫脑电信号图Ⅰ(n=8)')
# plt.show()
# fn.append(fn_1)
#
# temp_1,fitted_value_1,yk_1,fn_1 = process(epilepsy_1,20)
# plt.plot(temp_1,epilepsy_1,'g',temp_1,yk_1,'b',temp_1,fitted_value_1,'r--')
# plt.title('去趋势之后的癫痫脑电信号图Ⅰ(n=20)')
# plt.show()
# fn.append(fn_1)
#
# temp_1,fitted_value_1,yk_1,fn_1 = process(epilepsy_1,50)
# plt.plot(temp_1,epilepsy_1,'g',temp_1,yk_1,'b',temp_1,fitted_value_1,'r--')
# plt.title('去趋势之后的癫痫脑电信号图Ⅰ(n=50)')
# plt.show()
# fn.append(fn_1)
#
# temp_1,fitted_value_1,yk_1,fn_1 = process(epilepsy_1,100)
# plt.plot(temp_1,epilepsy_1,'g',temp_1,yk_1,'b',temp_1,fitted_value_1,'r--')
# plt.title('去趋势之后的癫痫脑电信号图Ⅰ(n=100)')
# plt.show()
# fn.append(fn_1)
#
# temp_1,fitted_value_1,yk_1,fn_1 = process(epilepsy_1,200)
# plt.plot(temp_1,epilepsy_1,'g',temp_1,yk_1,'b',temp_1,fitted_value_1,'r--')
# plt.title('去趋势之后的癫痫脑电信号图Ⅰ(n=200)')
# plt.show()
# fn.append(fn_1)
#
# temp_1,fitted_value_1,yk_1,fn_1 = process(epilepsy_1,500)
# plt.plot(temp_1,epilepsy_1,'g',temp_1,yk_1,'b',temp_1,fitted_value_1,'r--')
# plt.title('去趋势之后的癫痫脑电信号图Ⅰ(n=500)')
# plt.show()
# fn.append(fn_1)
#
# temp_1,fitted_value_1,yk_1,fn_1 = process(epilepsy_1,1000)
# plt.plot(temp_1,epilepsy_1,'g',temp_1,yk_1,'b',temp_1,fitted_value_1,'r--')
# plt.title('去趋势之后的癫痫脑电信号图Ⅰ(n=1000)')
# plt.show()
# fn.append(fn_1)
#
# number = [4,8,20,50,100,200,500,1000]
# number_log = []
# fn_log = []
# for i in range(0,len(number)):
#     number_log.append(math.log(number[i],10))
#     fn_log.append(math.log(fn[i],10))
#
# poly = np.polyfit(number_log, fn_log, deg = 1)
#
# plt.plot(number_log, fn_log,'o')
# plt.plot(number_log, np.polyval(poly,number_log))
# plt.show()
#
# fn_normal_1 = []
# temp_1,fitted_value_1,yk_1,fn_1 = process(normal_1,4)
# fn_normal_1.append(fn_1)
# temp_1,fitted_value_1,yk_1,fn_1 = process(normal_1,8)
# fn_normal_1.append(fn_1)
# temp_1,fitted_value_1,yk_1,fn_1 = process(normal_1,20)
# fn_normal_1.append(fn_1)
# temp_1,fitted_value_1,yk_1,fn_1 = process(normal_1,50)
# fn_normal_1.append(fn_1)
# temp_1,fitted_value_1,yk_1,fn_1 = process(normal_1,100)
# fn_normal_1.append(fn_1)
# temp_1,fitted_value_1,yk_1,fn_1 = process(normal_1,200)
# fn_normal_1.append(fn_1)
# temp_1,fitted_value_1,yk_1,fn_1 = process(normal_1,500)
# fn_normal_1.append(fn_1)
# temp_1,fitted_value_1,yk_1,fn_1 = process(normal_1,1000)
# fn_normal_1.append(fn_1)
#
# fn_normal_log = []
# for i in range(0,len(number)):
#     fn_normal_log.append(math.log(fn_normal_1[i],10))
# poly = np.polyfit(number_log, fn_log, deg = 1)
# plt.plot(number_log, fn_normal_log,'o')
# plt.plot(number_log, np.polyval(poly,number_log))
#

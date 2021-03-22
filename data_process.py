import  split_list
import  math
import numpy as np

def process(variable_name,group_count):
    ave_value = []
    variable_sum = 0
    for i in range(0, len(variable_name)):
        variable_sum += variable_name[i]
    ave = variable_sum / len(variable_name)
    for i in range(0, len(variable_name)):
        ave_value.append(variable_name[i] - ave)
    yi = np.cumsum(ave_value)  # yi是文献中的y(k)

    temp = []
    for i in range(0, len(variable_name)):
        temp.append(i)
    x_data1 = split_list.list_of_groups(temp, group_count)
    y_data1 = split_list.list_of_groups(yi, group_count)  # y_data1 = yi
    temp1 = []
    for i in range(0, int(len(variable_name)/group_count)):
        poly = np.polyfit(x_data1[i], y_data1[i], deg=1)
        temp2 = np.polyval(poly, x_data1[i])
        for j in range(0, group_count):
            temp1.append(temp2[j])

    y_data2 = split_list.list_of_groups(temp1, group_count)  # 去趋势之后的函数值 yk
    yk_minus = []
    t = []
    a = 0
    for i in range(0, int(len(variable_name)/group_count)):
        yk_minus.append(list(map(lambda x: x[0] - x[1], zip(y_data1[i], y_data2[i]))))
        for j in range(0, group_count):
            t.append(yk_minus[i][j])

    for i in range(0,len(t)):
        a += (t[i])**2
    fn = math.sqrt(a / len(t))
    return temp,temp1,yi,fn

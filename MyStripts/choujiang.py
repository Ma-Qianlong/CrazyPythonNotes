import random as r_num  # 引入random库

#num = int(input('please enter the number of activity:'))

list_a = ['张', '邹', '马', '黄', '常', '李']
num = len(list_a)

r_num.seed()  # 设置随机数种子，这里为系统时间

run_count = 1;
i = 0;
while i < run_count:
    random_num = r_num.randint(0, num-1)  # 调用randint()函数取范围内的一个整数

    print('\nthe %02d dog: ' % (i+1))
    print('the random number :', random_num)
    print('the lucky dog is :' + list_a[random_num])  # end去除换行符

    i += 1


# avoid_exit = input()  # 防止闪退

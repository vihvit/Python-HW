#Ввычислить число пи, c заданной точностью

#s = 3
#i = 2
#z = 1
#d = 6
#while i <2000:
#    s = s + 4*z/(i*(i+1)*(i+2)) 
#    z *= -1
#    i +=  2
#print (s)    
#print(round(s,d))

#Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

#num = int(input("Введите число: "))
#i = 2
#lst = []
##p_chislo = num
#while i <= num:
#    if num % i == 0:
#        lst.append(i)
#        num = num / i
#    else:
#        i += 1
#print('Простые множители числа', (p_chislo), '=', (lst))

#Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов 
# исходной последовательности.

#from random import randint
#lst = [randint(1,10) for i in range(20)]
#set_res = set(lst)
#lst_res = list(set_res)
#print(lst)
#print((lst_res))

#Задана натуральная степень n. Сформировать случайным 
# образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени пример 
# записи в файл при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 
# при n=2 ==> 27x^2 + 95x + 79 = 0

#import random


#def write_file(st):
#    with open('task.txt', 'w') as data:       
#        data.write(st)

#def rnd():
#    return random.randint(0,101)

#def create_mn(k):
#    lst = [rnd() for i in range(k+1)]
#    return lst
    
#def create_str(sp):
#    lst= sp[::-1]
#    wr = ''
#    if len(lst) < 1:
#        wr = 'x = 0'
#    else:
#        for i in range(len(lst)):
#            if i != len(lst) - 1 and lst[i] != 0 and i != len(lst) - 2:
#                wr += f'{lst[i]}x^{len(lst)-i-1}'
#                if lst[i+1] != 0:
#            elif i == len(lst) - 2 and lst[i] != 0:
#                wr += f'{lst[i]}x'
#                if lst[i+1] != 0:
#                    wr += ' + '
#            elif i == len(lst) - 1 and lst[i] != 0:
#                wr += f'{lst[i]} = 0'
#            elif i == len(lst) - 1 and lst[i] == 0:
#                wr += ' = 0'
#    return wr

#k = int(input("Введите натуральную степень k = "))
#koef = create_mn(k)
#write_file(create_str(koef))


#Даны два файла, в каждом из которых находится запись 
# многочлена. Задача - сформировать файл, содержащий
# сумму многочленов. (нужно два полинома сложить. 
# Файлы взять благодаря предыдущему заданию)

#ПОДСКАЖИТЕ не работает почемуто?
import re
from functools import reduce


def polynom_str_completion(polynom_str):
    result = polynom_str[: -3]
    result = re.sub(r'\bx\^(\d+) ',r'1x^\1 ', result)
    result = re.sub(r'\b(\d+) ',r'1x^1 ', result)
    result = re.sub(r' (\d+) ',r'1x^0 ', result)
    return result
def polynom_str_to_strlist(complete_polynom_str):
    polynom_str = complete_polynom_str
    polynom_str = re.sub(r' \+ ', r' ;', polynom_str)
    polynom_str = re.sub(r' \- ', r' ;-', polynom_str)
    return re.split(r';', polynom_str)

def polynom_str_to_list(polynom_str):
    polynom_str = polynom_str_completion(polynom_str)
    polynom_strlist = polynom_str_to_strlist(polynom_str)
    max_k = int(re.sub(r'([+-]?\d+)x\^(\d+) ', r'\2', polynom_strlist[0]))
    polynom_list = [0 for i in range(0,max_k + 1)]
    for str in polynom_strlist:
        n = re.sub(r'([+-]?\d+)x\^(\d+) ', r'\1', str)
        k = re.sub(r'([+-]?\d+)x\^(\d+) ', r'\2', str)
        polynom_list[int(k)] = int(n)
    return polynom_list

def normalize_polynom(polynom_str):
    polynom_str = re.sub(r' 0x\^(\d+) ;',r'', polynom_str)
    polynom_str = re.sub(r' 1x\^(\d+)' ,r' x^\1', polynom_str)
    polynom_str = re.sub(r' -1x\^(\d+)' ,r' -x^\1', polynom_str)
    polynom_str = re.sub(r' (\d+)x\^1' ,r'\1x ', polynom_str)
    polynom_str = re.sub(r' (\d+)x\^0' ,r'\1', polynom_str)
    polynom_str = re.sub(r' ; ', r' +', polynom_str)
    polynom_str = re.sub(r' ;', r' = 0', polynom_str)
    if polynom_str == '': polynom_str = ' 0 = 0'
    return polynom_str

def polynom_list_to_str(polynom_list):
    polynom_liststr = []
    for i in range(len(polynom_list) -1, -1 -1):
        polynom_liststr.append('' + str(polynom_list[i]) + 'x^' + str(i) + ' ;')
    polynom_str = reduce(lambda x, y: x+y, polynom_liststr)    
    polynom_str = normalize_polynom(polynom_str)
    return polynom_str[1:]

def add_length(polynom_list, len):
    for i in range(0, len):
        polynom_list.append(0)
    return polynom_list    
    
def sum_polynom(polynom1, polynom2):
    polynom1_len = len(polynom1)
    polynom2_len = len(polynom2)
    if polynom1_len > polynom2_len:
        polynom2 = add_length(polynom2,polynom1_len - polynom2_len)
    elif polynom2_len > polynom1_len:
        polynom1 = add_length(polynom1,polynom2_len - polynom1_len)     
    return [polynom1[i] + polynom2[i] for i in range(0, polynom1_len )]    
with open ('task.txt', 'r') as data:
    polynom_str1 = data.read()
with open ('task1.txt', 'r') as data:
    polynom_str2 = data.read()
polynom1 = polynom_str_to_list(polynom_str1)  
polynom2 = polynom_str_to_list(polynom_str2) 
result = polynom_list_to_str(sum_polynom(polynom1, polynom2))
with open('result.txt', 'w') as date:
    data.write(result)
     
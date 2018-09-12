from helper import *

inpu_data = read_input('LS_Group05/Class1.txt')
train_data,test_data = part_data(inpu_data)
mean,variance = get_stats(train_data)

a = []
b = transpose(a)
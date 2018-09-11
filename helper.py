import random

def read_input(s):
    file = open(s)
    return_array = []
    a = file.readline()
    while(a):
        d = map(float,a.split())
        d = tuple(d)
        return_array.append(d)
        a = file.readline()
    return return_array

def part_data(a):
    random.shuffle(a)
    partition = int(len(a)*0.75)
    return a[:partition],a[partition:]

def get_stats(a):
    mean = [0,0]
    variance = [0,0]
    for i in a:
        mean[0] += i[0]
        mean[1] += i[1]
        variance[0] += pow(i[0],2)
        variance[1] += pow(i[1],2)
    mean[0] /= len(a)
    mean[1] /= len(a)
    variance[0] /= len(a)
    variance[1] /= len(a)
    variance[0] -= pow(mean[0],2)
    variance[1] -= pow(mean[1],2)
    return (mean,variance)

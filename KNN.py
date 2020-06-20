import csv
import random
#读取
with open('Prostate_Cancer.csv','r') as file:
    reader = csv.DictReader(file)
    datas = [row for row in reader]
#分组
print(datas)
random.shuffle(datas)
n = len(datas)//3
test_set = datas[0: n]
train_set = datas[n:]
#KNN
#距离
def distance(d1,d2):
    res = 0
    for key in('radius','texture','perimeter','area','smoothness','compactness','symmetry','fractal_dimension'):
        res += (float(d1[key]) - float(d2[key]))**2
    return res**0.5

K= 5
def Knn(data):
    res = [
        {'result': train['diagnosis_result'], 'distance':distance(data, train)}
        for train in train_set
    ]
    #print(res)
    res =  sorted(res, key = lambda item: item['distance'])

    res2 = res[0:K]

    result = {'B': 0, 'M': 0}
    sum = 0
    for r in res2:
        sum+=r['distance']
    for r in res2:
        result[r['result']] += 1- r['distance']/sum
    #print(result)
    #print(data['diagnosis_result'])
    if result['B']> result['M']:
        return 'B'
    else:
        return 'M'

correct=0
for test in test_set:
    result = test['diagnosis_result']
    result2 = Knn(test)
    if result == result2:
        correct += 1
print("准确率 =", end='')
print(format(100*correct/len(test_set)),end='')
print('%')

print(datas)

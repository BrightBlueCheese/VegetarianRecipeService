import random

# train 1만 epoch 에 약 2시간 소요!!
train_num = 22000
test_num = 7000

for i in range(train_num):
    with open('yolov4/darknet_master/custom_data/train.txt','r') as source:
        data = [ (random.random(), line) for line in source ]
    data.sort()
    with open('yolov4/darknet_master/custom_data/train.txt','w') as target:
        for _, line in data:
            target.write( line )

    if i  % 100 == 0:
        print(f'train.txt: {i} - process')
    elif i == train_num-1:
        print(f'train.txt: done')


for i in range(test_num):
    with open('yolov4/darknet_master/custom_data/test.txt','r') as source:
        data = [ (random.random(), line) for line in source ]
    data.sort()
    with open('yolov4/darknet_master/custom_data/test.txt','w') as target:
        for _, line in data:
            target.write( line )

    if i  % 100 == 0:
        print(f'test.txt: {i} - process')
    elif i == test_num-1:
        print(f'test.txt: done')


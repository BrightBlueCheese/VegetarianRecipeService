import os
import random
import shutil
import json 

label_dict = {'가리비': 0, '가지': 1, '감자': 2, '게맛살': 3, '고구마': 4, '고등어': 5, '고추': 6, '고추장': 7, 
            '그린올리브': 8, '김': 9, '꼬막': 10, '느타리버섯': 11, '다시마': 12, '단호박': 13, '달걀': 14, '당근': 15, 
            '대파': 16, '두부': 17, '땅콩버터': 18, '랍스타': 19, '레몬': 20, '로메인상추': 21, '리코타치즈': 22, 
            '마늘': 23, '마요네즈': 24, '만두': 25, '무우': 26, '문어': 27, '바게트': 28, '밥': 29, '방울토마토': 30, 
            '배추': 31, '배추김치': 32, '버터': 33, '베이글': 34, '브로콜리': 35, '블루베리': 36, '사과': 37, '새우': 38, 
            '샐러리': 39, '소면': 40, '숙주나물': 41, '스파게티면': 42, '시금치': 43, '아몬드': 44, '아보카도': 45, 
            '애호박': 46, '양배추': 47, '양파': 48, '연근': 49, '오이': 50, '오징어': 51, '와플': 52, '우유': 53, 
            '잡곡식빵': 54, '전복': 55, '체다치즈': 56, '치커리': 57, '칠리소스': 58, '케일': 59, '케첩': 60, '토마토': 61, 
            '토마토파스타소스': 62, '파슬리': 63, '파인애플': 64, '파프리카': 65, '팽이버섯': 66, '표고버섯': 67, '호두': 68,
            '양송이버섯': 69}
# 양송이는 나중에 추가 됨




""" 
# 함수 실행 코드 주석처리 됨
# 변수 target_folder 에 값 할당 안된게 정상
"""
def augmented_txt_label_changer(target_txt, train_or_valid):

    if train_or_valid == 'train':
        target_txt = f'./roboflow/{target_folder}/train/{target_txt}'
    elif train_or_valid == 'valid':
        target_txt = f'./roboflow/{target_folder}/valid/{target_txt}'
    with open(target_txt, 'r', encoding='UTF-8') as f:
        txt_lines = f.readlines()
        save_txt_lines = []
        for txt_line in txt_lines:
            save_txt_lines.append(txt_line.replace('\n',''))

    revised_txt_line_list = []

    for i in save_txt_lines:
        splited_txt_list = i.split(' ')
        splited_txt_list[0] = str(label_dict[target_folder])
        revised_txt_line = ' '.join(splited_txt_list)
        revised_txt_line_list.append(revised_txt_line)

    # print(revised_txt_line_list)

    with open(target_txt, 'w', encoding='UTF-8') as f:
        for revised_txt_line_v2 in revised_txt_line_list:
            f.write(revised_txt_line_v2 + '\n')

def get_files_count(folder_path):
    file_count = 0
    for t_or_v in ['train', 'valid']:
        dirListing = len([_ for _ in os.listdir(f'{folder_path}{t_or_v}') if _.endswith('.jpg')])
        file_count += dirListing
    return file_count




def train_test_split_augmented_swish_data(folder_path):
    
    folder_train = folder_path + 'train/'
    folder_valid = folder_path + 'valid/'


    # train 폴더에 있는 txt 파일만 받아오기
    file_txt_from_train = [_ for _ in os.listdir(folder_train) if _.endswith('.txt')]

    # valid 폴더에 있는 txt 파일만 받아오기
    file_txt_from_valid = [_ for _ in os.listdir(folder_valid) if _.endswith('.txt')]
    count = 0

    # train or valid
    for train_or_valid_case in ['train', 'valid']:
        if train_or_valid_case == 'train':
            file_txt_from_folder = [_ for _ in os.listdir(folder_train) if _.endswith('.txt')]
        elif train_or_valid_case == 'valid':
            file_txt_from_folder = [_ for _ in os.listdir(folder_valid) if _.endswith('.txt')]

        for file in file_txt_from_folder:
            # file_name_txt = 
            file_name_txt = file

            augmented_txt_label_changer(file_name_txt, train_or_valid_case)
            file_name_jpg = file.split('.txt')[0] + '.jpg'

            origin_txt = f'./roboflow/{target_folder}/{train_or_valid_case}/{file_name_txt}'
            origin_img = f'./roboflow/{target_folder}/{train_or_valid_case}/{file_name_jpg}'

            # 원본
            copy_to_images_dir_txt = f'./yolov4_swish/darknet_master/custom_data/images/{file_name_txt}'
            copy_to_labels_dir_txt = f'./yolov4_swish/darknet_master/custom_data/labels/{file_name_txt}'
            copy_to_image_dir_img = f'./yolov4_swish/darknet_master/custom_data/images/{file_name_jpg}'

            # # 임시
            # copy_to_images_dir_txt = f'./aug_practice_swish/images/{file_name_txt}'
            # copy_to_labels_dir_txt = f'./aug_practice_swish/labels/{file_name_txt}'
            # copy_to_image_dir_img = f'./aug_practice_swish/images/{file_name_jpg}'


            # train images
            
            # 원본
            if train_or_valid_case == 'valid':
                train_or_valid_case = 'test'
            train_or_valid_data_loader_txt = f'./yolov4_swish/darknet_master/custom_data/{train_or_valid_case}.txt'

            

            # # 임시
            # train_or_valid_data_loader_txt = f'./aug_practice_swish/{train_or_valid_case}.txt'

            # data loader에 data 경로 삽입
            with open(train_or_valid_data_loader_txt, 'a', encoding='UTF-8') as f:
                f.write('custom_data/images/' + file_name_jpg + '\n')
            
            if train_or_valid_case == 'test':
                train_or_valid_case = 'valid'

            count += 1




            shutil.copy(origin_txt, copy_to_images_dir_txt)
            shutil.copy(origin_txt, copy_to_labels_dir_txt)
            shutil.copy(origin_img, copy_to_image_dir_img)
            
            if count == 1 or count % 10 == 0:
                print(f'working on {target_folder} -- {count} steps')

if __name__ == "__main__":

    # 인덱스 지정
    # target_folder_list = list(label_dict.keys())[:인덱스숫자]
    
    # 전체 다 하기
    target_folder_list = list(label_dict.keys())

    # 실수 방지용
    # target_folder_list = ['실수 방지']

    print(target_folder_list)
    process_record_list = []
    for target_folder in target_folder_list:

        augmented_swish_file_path = f'./roboflow/{target_folder}/'

        file_len = get_files_count(augmented_swish_file_path)

        train_test_split_augmented_swish_data(augmented_swish_file_path)

        process_record = f'{target_folder}의 파일: {file_len}'
        process_record_list.append(process_record)
    
    print('train_test_split 결과')
    for i in process_record_list:
        print('=================================================')
        print(i)



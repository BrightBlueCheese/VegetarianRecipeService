import os
import random
import shutil
import json 

label_dict = {'가리비': 0, '가지': 1, '게맛살': 2, '고구마': 3, '고등어': 4, '고추': 5, '고추장': 6, '그린올리브': 7, '김': 8, 
            '꼬막': 9, '녹색피망': 10, '느타리버섯': 11, '다시마': 12, '단호박': 13, '달걀': 14, '당근': 15, '대파': 16, 
            '두부': 17, '땅콩버터': 18, '랍스타': 19, '레몬': 20, '로메인상추': 21, '리코타치즈': 22, '마늘': 23, '마요네즈': 24, 
            '만두': 25, '명란젓': 26, '모짜렐라치즈': 27, '무우': 28, '문어': 29, '물미역': 30, '바게트': 31, '밥': 32, 
            '방울토마토': 33, '배추': 34, '배추김치': 35, '버섯': 36, '버터': 37, '베이글': 38, '브로콜리': 39, '삶은달걀': 40, 
            '새우': 41, '샐러리': 42, '생크림': 43, '소면': 44, '스파게티면': 45, '양배추': 46, '연근': 47, '와플': 48, '우유': 49, 
            '잡곡식빵': 50, '적양배추': 51, '전복': 52, '체다치즈': 53, '치커리': 54, '칠리소스': 55, '케일': 56, '케첩': 57, 
            '토마토': 58, '토마토파스타소스': 59, '파슬리': 60, '파인애플': 61, '파프리카': 62, '팽이버섯': 63, '표고버섯': 64,
            '숙주나물': 65, '슬라이스치즈': 66, '시금치': 67, '아보카도': 68, '애호박': 69, '양파':70, '오이':71, '오징어':72,
            '아몬드':73, '사과':74, '블루베리': 75, '호두': 76}



label_dict = {'가리비': 0, '가지': 1, '게맛살': 2, '고구마': 3, '고등어': 4, '고추': 5, '고추장': 6, '그린올리브': 7, '김': 8, 
            '꼬막': 9, '느타리버섯': 11, '다시마': 12, '단호박': 13, '달걀': 14, '당근': 15, '대파': 16, 
            '두부': 17, '땅콩버터': 18, '랍스타': 19, '레몬': 20, '로메인상추': 21, '리코타치즈': 22, '마늘': 23, '마요네즈': 24, 
            '만두': 25, '명란젓': 26, '모짜렐라치즈': 27, '무우': 28, '문어': 29, '물미역': 30, '바게트': 31, '밥': 32, 
            '방울토마토': 33, '배추': 34, '배추김치': 35, '버터': 37, '베이글': 38, '브로콜리': 39, 
            '새우': 41, '샐러리': 42, '소면': 44, '스파게티면': 45, '양배추': 46, '연근': 47, '와플': 48, '우유': 49, 
            '잡곡식빵': 50, '적양배추': 51, '전복': 52, '체다치즈': 53, '치커리': 54, '칠리소스': 55, '케일': 56, '케첩': 57, 
            '토마토': 58, '토마토파스타소스': 59, '파슬리': 60, '파인애플': 61, '파프리카': 62, '팽이버섯': 63, '표고버섯': 64,
            '숙주나물': 65, '시금치': 67, '아보카도': 68, '애호박': 69, '양파':70, '오이':71, '오징어':72,
            '아몬드':73, '사과':74, '블루베리': 75, '호두': 76}

# label_dict = {'게맛살':0, '마늘 - 복사본':1, '소면':2}
augmented_list = ['마늘', '명란젓', '문어', '배추', '배추김치', '버섯', '생크림', '소면', '연근', '와플', '치커리', '파슬리' ,'팽이버섯']

""" 
# 함수 실행 코드 주석처리 됨
# 변수 target_folder 에 값 할당 안된게 정상
"""
def augmented_txt_label_changer(target_txt):
    target_txt = f'./dataset_process/{target_folder}/{target_folder}/{target_txt}'
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
	dirListing = os.listdir(folder_path)
	return len(dirListing)

def get_txt_files_count(folder_path):
    folder_of_img = folder_path
    file_txt_only = [_ for _ in os.listdir(folder_of_img) if _.endswith('.txt')]
    return len(file_txt_only)

def train_test_split_over_2200(folder_path):
    folder_of_json = folder_path + f'{target_folder} json'

    # json 파일만 리스트로 받아오기
    files_json = [_ for _ in os.listdir(folder_of_json) if _.endswith('.json')]
    count = 0
    for file in files_json[:2200]: # [:2200]
        save_json_data = []
        path = os.path.join(folder_of_json, file)
        with open(path, 'r', encoding='utf-8') as f:
            json_contents = f.read()
            json_data = json.loads(json_contents)
            # print(*json_data)
            # print()
            texted_annotation = []
            for i in range(len(json_data)):
                data = json_data[i]
                x, y, w, h = data['Point(x,y)'].split(',')[0], data['Point(x,y)'].split(',')[1], data['W'], data['H']
                # print(f'{x}, {y}, {w}, {h}')

                # 여기다 이미지 클래스 라벨 번호도 써야 함
                texted_annotation.append(f'{label_dict[target_folder]} {x} {y} {w} {h}')
        with open(path.split('.json')[0] + '.txt', 'w', encoding='UTF-8') as f:
            for annotation in texted_annotation:
                f.write(annotation + '\n')
        # target_text = path.split('.json')[0] + '.txt'
        # copy text file
        file_name_txt = data['Code Name'].split('.')[0] + '.txt'
        file_name_jpg = data['Code Name']
        origin_txt = path.split('.json')[0] + '.txt'
        origin_img = f'./dataset_process/{target_folder}/{target_folder}/{file_name_jpg}'
        
        # 원본
        copy_to_images_dir_txt = f'./yolov4/darknet_master/custom_data/images/{file_name_txt}'
        copy_to_labels_dir_txt = f'./yolov4/darknet_master/custom_data/labels/{file_name_txt}'
        copy_to_image_dir_img = f'./yolov4/darknet_master/custom_data/images/{file_name_jpg}'

        # # 임시
        # copy_to_images_dir_txt = f'./aug_practice/images/{file_name_txt}'
        # copy_to_labels_dir_txt = f'./aug_practice/labels/{file_name_txt}'
        # copy_to_image_dir_img = f'./aug_practice/images/{file_name_jpg}'

        # put image dir into train set until 2000
        if count < 2000:
            # 원본
            train_txt_file = f'./yolov4/darknet_master/custom_data/train.txt'

            # # 임시
            # train_txt_file = f'./aug_practice/train.txt'

            with open(train_txt_file, 'a', encoding='UTF-8') as f:
                f.write('custom_data/images/' + file_name_jpg + '\n')
            count += 1
        else:
            # 원본
            test_txt_file = f'./yolov4/darknet_master/custom_data/test.txt'

            # # 임시
            # test_txt_file = f'./aug_practice/test.txt'

            with open(test_txt_file, 'a', encoding='UTF-8') as f:
                f.write('custom_data/images/' + file_name_jpg + '\n')
            count += 1


        shutil.copy(origin_txt, copy_to_images_dir_txt)
        shutil.copy(origin_txt, copy_to_labels_dir_txt)
        shutil.copy(origin_img, copy_to_image_dir_img)

        if count == 1 or count % 100 == 0:
            print(f'working on {target_folder} -- {count} steps')


def train_test_split_under_2200(folder_path, file_len, split_ratio=0.2):
    folder_of_json = folder_path + f'{target_folder} json'

    # json 파일만 리스트로 받아오기
    files_json = [_ for _ in os.listdir(folder_of_json) if _.endswith('.json')]
    count = 0

    split_benchmark_int = int(len(files_json) - len(files_json)*split_ratio)
    for file in files_json: 
        save_json_data = []
        path = os.path.join(folder_of_json, file)
        with open(path, 'r', encoding='utf-8') as f:
            json_contents = f.read()
            json_data = json.loads(json_contents)
            # print(*json_data)
            texted_annotation = []
            for i in range(len(json_data)):
                data = json_data[i]
                x, y, w, h = data['Point(x,y)'].split(',')[0], data['Point(x,y)'].split(',')[1], data['W'], data['H']
                # print(f'{x}, {y}, {w}, {h}')

                # 여기다 이미지 클래스 라벨 번호도 써야 함
                texted_annotation.append(f'{label_dict[target_folder]} {x} {y} {w} {h}')
        with open(path.split('.json')[0] + '.txt', 'w', encoding='UTF-8') as f:
            for annotation in texted_annotation:
                f.write(annotation + '\n')
        # target_text = path.split('.json')[0] + '.txt'
        # copy text file
        file_name_txt = data['Code Name'].split('.')[0] + '.txt'
        file_name_jpg = data['Code Name']
        origin_txt = path.split('.json')[0] + '.txt'
        origin_img = f'./dataset_process/{target_folder}/{target_folder}/{file_name_jpg}'
        

        # 원본
        copy_to_images_dir_txt = f'./yolov4/darknet_master/custom_data/images/{file_name_txt}'
        copy_to_labels_dir_txt = f'./yolov4/darknet_master/custom_data/labels/{file_name_txt}'
        copy_to_image_dir_img = f'./yolov4/darknet_master/custom_data/images/{file_name_jpg}'

        # # 임시
        # copy_to_images_dir_txt = f'./aug_practice/images/{file_name_txt}'
        # copy_to_labels_dir_txt = f'./aug_practice/labels/{file_name_txt}'
        # copy_to_image_dir_img = f'./aug_practice/images/{file_name_jpg}'
        
        # put image dir into train set until 2000
        if count <= split_benchmark_int:
            # 원본
            train_txt_file = f'./yolov4/darknet_master/custom_data/train.txt'

            # # 임시
            # train_txt_file = f'./aug_practice/train.txt'

            with open(train_txt_file, 'a', encoding='UTF-8') as f:
                f.write('custom_data/images/' + file_name_jpg + '\n')
            count += 1
        else:
            # 원본
            test_txt_file = f'./yolov4/darknet_master/custom_data/test.txt'

            # # 임시
            # test_txt_file = f'./aug_practice/test.txt'

            with open(test_txt_file, 'a', encoding='UTF-8') as f:
                f.write('custom_data/images/' + file_name_jpg + '\n')
            count += 1


        shutil.copy(origin_txt, copy_to_images_dir_txt)
        shutil.copy(origin_txt, copy_to_labels_dir_txt)
        shutil.copy(origin_img, copy_to_image_dir_img)
        
        if count == 1 or count % 100 == 0:
            print(f'working on {target_folder} -- {count} steps')


def train_test_split_augmented_data(folder_path, txt_file_len, split_ratio=0.2):
    folder_of_txt = folder_path + f'{target_folder}'

    # 이미지 폴더에 있는 txt 파일만 받아오기
    file_txt_from_imgdir = [_ for _ in os.listdir(folder_of_txt) if _.endswith('.txt')]
    count = 0

    split_benchmark_int = int(len(file_txt_from_imgdir) - len(file_txt_from_imgdir)*split_ratio)

    for file in file_txt_from_imgdir:
        # file_name_txt = 
        file_name_txt = file
        augmented_txt_label_changer(file_name_txt)
        file_name_jpg = file.split('.txt')[0] + '.jpg'

        origin_txt = f'./dataset_process/{target_folder}/{target_folder}/{file_name_txt}'
        origin_img = f'./dataset_process/{target_folder}/{target_folder}/{file_name_jpg}'

        # 원본
        copy_to_images_dir_txt = f'./yolov4/darknet_master/custom_data/images/{file_name_txt}'
        copy_to_labels_dir_txt = f'./yolov4/darknet_master/custom_data/labels/{file_name_txt}'
        copy_to_image_dir_img = f'./yolov4/darknet_master/custom_data/images/{file_name_jpg}'

        # # 임시
        # copy_to_images_dir_txt = f'./aug_practice/images/{file_name_txt}'
        # copy_to_labels_dir_txt = f'./aug_practice/labels/{file_name_txt}'
        # copy_to_image_dir_img = f'./aug_practice/images/{file_name_jpg}'

        # put image dir into train set until 2000
        if count <= split_benchmark_int:
            # 원본
            train_txt_file = f'./yolov4/darknet_master/custom_data/train.txt'

            # # 임시
            # train_txt_file = f'./aug_practice/train.txt'

            with open(train_txt_file, 'a', encoding='UTF-8') as f:
                f.write('custom_data/images/' + file_name_jpg + '\n')
            count += 1
        else:
            # 원본
            test_txt_file = f'./yolov4/darknet_master/custom_data/test.txt'

            # # 임시
            # test_txt_file = f'./aug_practice/test.txt'

            with open(test_txt_file, 'a', encoding='UTF-8') as f:
                f.write('custom_data/images/' + file_name_jpg + '\n')
            count += 1


        shutil.copy(origin_txt, copy_to_images_dir_txt)
        shutil.copy(origin_txt, copy_to_labels_dir_txt)
        shutil.copy(origin_img, copy_to_image_dir_img)
        
        if count == 1 or count % 100 == 0:
            print(f'working on {target_folder} -- {count} steps')

if __name__ == "__main__":

    # 딕셔너리에 있는거 몰아서 하기 
    # 한번에 돌리기 위해서는 file_match_test로 모든 폴더 한 번 순회 시켜줘야 함
    #     label_dict = {'파프리카':0, '녹색피망':1, '로메인상추':2 } 위에 선언 됨


    """
    # 최근에 이 코드로 돌림 0228
    # 실수로 실행 방지용
    target_folder_list = list(label_dict.keys())[73:]
    print(target_folder_list)
    process_record_list = []
    for target_folder in target_folder_list:

        file_path = f'./dataset_process/{target_folder}/'

        file_len = get_files_count(file_path + f'{target_folder} json/')
        txt_file_len = get_txt_files_count(file_path + f'{target_folder}')

        if file_len >= 2200 and target_folder not in augmented_list:
            train_test_split_over_2200(file_path)
        elif file_len < 2200 and target_folder not in augmented_list:
            train_test_split_under_2200(file_path, file_len)
        elif target_folder in augmented_list:
            train_test_split_augmented_data(file_path, txt_file_len)

        process_record = f'{target_folder}의 파일: {file_len}'
        process_record_list.append(process_record)
    
    print('train_test_split 결과')
    for i in process_record_list:
        print('=================================================')
        print(i)
    """






    # # 딕셔너리를 인덱스로 불러와서 하나씩 돌리기
    # target_folder = list(label_dict.keys())[1] 
    # file_path = f'./dataset_process/{target_folder}/'

    # file_len = get_files_count(file_path + f'{target_folder} json/')
    # txt_file_len = get_txt_files_count(file_path + f'{target_folder}')

    # if file_len >= 2200 and target_folder not in augmented_list:
    #     train_test_split_over_2200(file_path)
    # elif file_len < 2200 and target_folder not in augmented_list:
    #     train_test_split_under_2200(file_path, file_len)
    # elif target_folder in augmented_list:
    #     train_test_split_augmented_data(file_path, txt_file_len)

    # print(f'{target_folder}의 파일: {file_len}')
    #     # print(target_folder)

    # # './yolov4/darknet_master/custom_data/images/A260155XX_00001.txt'
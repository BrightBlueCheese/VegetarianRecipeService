import os
import collections 

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


def file_match_test(folder_path):
    folder_of_json = folder_path + f'{target_folder} json'
    folder_of_img = folder_path + f'{target_folder}'

    files_json = os.listdir(folder_of_json)
    files_img = os.listdir(folder_of_img)

    file_list = []
    for file in files_json:
        file_name = file.split('.')[0]
        file_list.append(file_name)
    for file in files_img:
        file_name = file.split('.')[0]
        file_list.append(file_name)
    
    file_count = collections.Counter(file_list)

    not_match = [k for k, v in file_count.items() if v == 1]
    print(not_match)

    deleted_count = 0

    # json지우기
    for file in not_match:
        file_to_delete = folder_of_json + '/' + file + '.json' 
        if os.path.isfile(file_to_delete):
            os.remove(file_to_delete)
            deleted_count += 1

    # # jpg 지우기
    # for file in not_match:
    #     file_to_delete = folder_of_img + '/' + file + '.jpg' 
    #     if os.path.isfile(file_to_delete):
    #         os.remove(file_to_delete)
    #         deleted_count += 1

    if len(not_match) == 0:
        print(f'No unmatched file')
    else:
        print(f'{deleted_count} files are removed from  {target_folder} json folder or are already removed.')

target_folder_list = list(label_dict.keys())[73:] # 숙주나물부터

for target_folder in target_folder_list:
    file_path = f'./dataset_process/{target_folder}/'

    file_match_test(file_path)
import os 

# dir_name_list 결과
"""
'가리비', '가지', '감자', '게맛살', '고구마', '고등어', '고추', '고추장', '그린올리브', '김', '꼬막', 
'느타리버섯', '다시마', '단호박', '달걀', '당근', '대파', '두부', '땅콩버터', '랍스타', '레몬', '로메인상추', 
'리코타치즈', '마늘', '마요네즈', '만두', '무우', '문어', '바게트', '밥', '방울토마토', '배추', '배추김치', 
'버터', '베이글', '브로콜리', '블루베리', '사과', '새우', '샐러리', '소면', '숙주나물', '스파게티면', 
'시금치', '아몬드', '아보카도', '애호박', '양배추', '양파', '연근', '오이', '오징어', '와플', 
'우유', '잡곡식빵', '전복', '체다치즈', '치커리', '칠리소스', '케일', '케첩', '토마토', '토마토파스타소스', 
'파슬리', '파인애플', '파프리카', '팽이버섯', '표고버섯', '호두'
"""
# 양송이는 나중에 추가 됨


def get_files_count(folder_path):
	dirListing = os.listdir(folder_path)
	return len(dirListing)

def print_files_in_dir(root_dir, prefix):
    # print('================')
    dir_name_list = []

    files = os.listdir(root_dir)

    for file in files:
        if not file.endswith('.labels'):
            path = os.path.join(root_dir, file)
            # print(prefix + path)
            dir_name_list.append(path.split('\\')[-1].split('.')[0])
            # print(path.split('/')[-1])


        # if os.path.isdir(path):
        #     print_files_in_dir(path, prefix + "    ")
    dir_name_list = sorted(list(set(dir_name_list)))
    print(dir_name_list)
    print(len(dir_name_list))

if __name__ == "__main__":
    # root_dir = "./ai_hub_food_dataset/Training/"
    root_dir = './dataset_process_swish'
    print_files_in_dir(root_dir, "")

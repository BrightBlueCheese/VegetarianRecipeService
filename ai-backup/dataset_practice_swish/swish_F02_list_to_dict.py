#  # dict_maker 결과
"""
label_dict = {'가리비': 0, '가지': 1, '감자': 2, '게맛살': 3, '고구마': 4, '고등어': 5, '고추': 6, '고추장': 7, 
            '그린올리브': 8, '김': 9, '꼬막': 10, '느타리버섯': 11, '다시마': 12, '단호박': 13, '달걀': 14, '당근': 15, 
            '대파': 16, '두부': 17, '땅콩버터': 18, '랍스타': 19, '레몬': 20, '로메인상추': 21, '리코타치즈': 22, 
            '마늘': 23, '마요네즈': 24, '만두': 25, '무우': 26, '문어': 27, '바게트': 28, '밥': 29, '방울토마토': 30, 
            '배추': 31, '배추김치': 32, '버터': 33, '베이글': 34, '브로콜리': 35, '블루베리': 36, '사과': 37, '새우': 38, 
            '샐러리': 39, '소면': 40, '숙주나물': 41, '스파게티면': 42, '시금치': 43, '아몬드': 44, '아보카도': 45, 
            '애호박': 46, '양배추': 47, '양파': 48, '연근': 49, '오이': 50, '오징어': 51, '와플': 52, '우유': 53, 
            '잡곡식빵': 54, '전복': 55, '체다치즈': 56, '치커리': 57, '칠리소스': 58, '케일': 59, '케첩': 60, '토마토': 61, 
            '토마토파스타소스': 62, '파슬리': 63, '파인애플': 64, '파프리카': 65, '팽이버섯': 66, '표고버섯': 67, '호두': 68}
"""



label_list = [
    '가리비', '가지', '감자', '게맛살', '고구마', '고등어', '고추', '고추장', '그린올리브', '김', '꼬막', 
    '느타리버섯', '다시마', '단호박', '달걀', '당근', '대파', '두부', '땅콩버터', '랍스타', '레몬', '로메인상추', 
    '리코타치즈', '마늘', '마요네즈', '만두', '무우', '문어', '바게트', '밥', '방울토마토', '배추', '배추김치', 
    '버터', '베이글', '브로콜리', '블루베리', '사과', '새우', '샐러리', '소면', '숙주나물', '스파게티면', 
    '시금치', '아몬드', '아보카도', '애호박', '양배추', '양파', '연근', '오이', '오징어', '와플', 
    '우유', '잡곡식빵', '전복', '체다치즈', '치커리', '칠리소스', '케일', '케첩', '토마토', '토마토파스타소스', 
    '파슬리', '파인애플', '파프리카', '팽이버섯', '표고버섯', '호두'
]

def dict_maker(label_list):
    label_dict = {}
    for i, label in enumerate(label_list):
        label_dict[label] = i
    return label_dict

if __name__ == "__main__":
    # print(label_list)
    print(dict_maker(label_list))
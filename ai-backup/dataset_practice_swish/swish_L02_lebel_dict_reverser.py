class_labels = ['scallop', 'eggplant', 'potato', 'crabstick', 'sweetpotato', 'mackerel', 'chili', 'gochujang', 'greenolive', 'koreangim', 
                'cockle', 'oystermushroom', 'kelp', 'sweetpumpkin', 'egg', 'carrot', 'koreanleek', 'tofu', 'peanutbutter', 'lobster', 'lemon', 
                'romaine', 'ricottacheese', 'garlic', 'mayonnaise', 'dumpling', 'radish', 'octopus', 'baquette', 'steamedrice', 'cherrytomato', 
                'napacabbage', 'napacabbagekimchi', 'butter', 'bagel', 'broccoli', 'blueberry', 'apple', 'shrimp', 'salary', 'plainnoodles', 
                'mungbeansprout', 'spaghettinoodles', 'spinach', 'almond', 'avocado', 'squash', 'cabbage', 'onion', 'lotusroot', 'cucumber', 
                'squid', 'waffle', 'milk', 'cerealbread', 'earsheel', 'cheddarcheese', 'chicory', 'chilisauce', 'kale', 'ketchup', 'tomato', 
                'tomatopastasauce', 'parsley', 'pineapple', 'paprika', 'enokimushroom', 'shiitakemushroom', 'walnut', 'whitemushroom']

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



"""
translated_dict = {'scallop': '가리비', 'eggplant': '가지', 'potato': '감자', 'crabstick': '게맛살', 'sweetpotato': '고구마', 'mackerel': '고등어', 
                'chili': '고추', 'gochujang': '고추장', 'greenolive': '그린올리브', 'koreangim': '김', 'cockle': '꼬막', 'oystermushroom': '느타리버섯', 
                'kelp': '다시마', 'sweetpumpkin': '단호박', 'egg': '달걀', 'carrot': '당근', 'koreanleek': '대파', 'tofu': '두부', 'peanutbutter': '땅콩버터', 
                'lobster': '랍스타', 'lemon': '레몬', 'romaine': '로메인상추', 'ricottacheese': '리코타치즈', 'garlic': '마늘', 'mayonnaise': '마요네즈', 
                'dumpling': '만두', 'radish': '무우', 'octopus': '문어', 'baquette': '바게트', 'steamedrice': '밥', 'cherrytomato': '방울토마토', 'napacabbage': '배추', 
                'napacabbagekimchi': '배추김치', 'butter': '버터', 'bagel': '베이글', 'broccoli': '브로콜리', 'blueberry': '블루베리', 'apple': '사과', 
                'shrimp': '새우', 'salary': '샐러리', 'plainnoodles': '소면', 'mungbeansprout': '숙주나물', 'spaghettinoodles': '스파게티면', 'spinach': '시금치', 
                'almond': '아몬드', 'avocado': '아보카도', 'squash': '애호박', 'cabbage': '양배추', 'onion': '양파', 'lotusroot': '연근', 'cucumber': '오이', 
                'squid': '오징어', 'waffle': '와플', 'milk': '우유', 'cerealbread': '잡곡식빵', 'earsheel': '전복', 'cheddarcheese': '체다치즈', 'chicory': '치커리', 
                'chilisauce': '칠리소스', 'kale': '케일', 'ketchup': '케첩', 'tomato': '토마토', 'tomatopastasauce': '토마토파스타소스', 'parsley': '파슬리', 
                'pineapple': '파인애플', 'paprika': '파프리카', 'enokimushroom': '팽이버섯', 'shiitakemushroom': '표고버섯', 'walnut': '호두', 'whitemushroom': '양송이버섯'}
"""

print(len(class_labels))

label_dict_key_list = list(label_dict.keys())

print(label_dict_key_list)

label_translated_dict = {}

for k, v in zip(class_labels, label_dict_key_list):
    label_translated_dict[k] = v


print(label_translated_dict)

# now move to label_translator.py

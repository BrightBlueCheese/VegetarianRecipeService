class_labels = ['scallop', 'eggplant', 'crabstick', 'sweetpotato', 'mackerel', 'chili', 'gochujang', 'greenolive', 'koreangim', 
                'cockle', 'greenbellpepper', 'oystermushroom', 'kelp', 'sweetpumpkin', 'egg', 'carrot', 'koreanleek', 'tofu', 
                'peanutbutter', 'lobster', 'lemon', 'romaine', 'ricottacheese', 'garlic', 'mayonnaise', 'dumpling', 
                'saltedpollackroe', 'mozzarellacheese', 'radish', 'octopus', 'seaweed', 'baquette', 'steamedrice', 'cherrytomato', 
                'napacabbage', 'napacabbagekimchi', 'mushroom', 'butter', 'bagel', 'broccoli', 'boiledegg', 'shrimp', 'salary', 
                'freshcream', 'plainnoodles', 'spaghettinoodles', 'cabbage', 'lotusroot', 'waffle', 'milk', 'cerealbread', 
                'redcabbage', 'earsheel', 'cheddarcheese', 'chicory', 'chilisauce', 'kale', 'ketchup', 'tomato', 'tomatopastasauce', 
                'parsley', 'pineapple', 'paprika', 'enokimushroom', 'shiitakemushroom', 'mungbeansprout', 'slicecheese', 'spinach', 
                'avocado', 'squash', 'onion', 'cucumber', 'squid', 'almond', 'apple', 'blueberry', 'walnut']

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



"""
translated_dict = {'scallop': '가리비', 'eggplant': '가지', 'crabstick': '게맛살', 'sweetpotato': '고구마', 'mackerel': '고등어', 
                'chili': '고추', 'gochujang': '고추장', 'greenolive': '그린올리브', 'koreangim': '김', 'cockle': '꼬막', 
                'greenbellpepper': '녹색피망', 'oystermushroom': '느타리버섯', 'kelp': '다시마', 'sweetpumpkin': '단호박', 'egg': '달걀', 
                'carrot': '당근', 'koreanleek': '대파', 'tofu': '두부', 'peanutbutter': '땅콩버터', 'lobster': '랍스타', 'lemon': '레몬', 
                'romaine': '로메인상추', 'ricottacheese': '리코타치즈', 'garlic': '마늘', 'mayonnaise': '마요네즈', 'dumpling': '만두', 
                'saltedpollackroe': '명란젓', 'mozzarellacheese': '모짜렐라치즈', 'radish': '무우', 'octopus': '문어', 'seaweed': '물미역', 
                'baquette': '바게트', 'steamedrice': '밥', 'cherrytomato': '방울토마토', 'napacabbage': '배추', 'napacabbagekimchi': '배추김치', 
                'mushroom': '버섯', 'butter': '버터', 'bagel': '베이글', 'broccoli': '브로콜리', 'boiledegg': '삶은달걀', 'shrimp': '새우', 
                'salary': '샐러리', 'freshcream': '생크림', 'plainnoodles': '소면', 'spaghettinoodles': '스파게티면', 'cabbage': '양배추', 
                'lotusroot': '연근', 'waffle': '와플', 'milk': '우유', 'cerealbread': '잡곡식빵', 'redcabbage': '적양배추', 'earsheel': '전복', 
                'cheddarcheese': '체다치즈', 'chicory': '치커리', 'chilisauce': '칠리소스', 'kale': '케일', 'ketchup': '케첩', 'tomato': '토마토', 
                'tomatopastasauce': '토마토파스타소스', 'parsley': '파슬리', 'pineapple': '파인애플', 'paprika': '파프리카', 'enokimushroom': '팽이버섯', 
                'shiitakemushroom': '표고버섯', 'mungbeansprout': '숙주나물', 'slicecheese': '슬라이스치즈', 'spinach': '시금치', 
                'avocado': '아보카도', 'squash': '애호박', 'onion': '양파', 'cucumber': '오이', 'squid': '오징어', 'almond': '아몬드', 
                'apple': '사과', 'blueberry': '블루베리', 'walnut': '호두'}
"""


print(len(class_labels))

label_dict_key_list = list(label_dict.keys())

print(label_dict_key_list)

label_translated_dict = {}

for k, v in zip(class_labels, label_dict_key_list):
    label_translated_dict[k] = v


print(label_translated_dict)

# now move to label_translator.py

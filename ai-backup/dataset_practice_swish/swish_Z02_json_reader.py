import json


file_path = './swish_predict_70_classes/predicted_result.json'

with open(file_path, 'r', encoding='utf-8') as f:
    json_contents = f.read()
    json_data = json.loads(json_contents)
    print(json_data)
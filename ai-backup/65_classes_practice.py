# -*- coding: utf-8 -*-
"""

@author: abhilash
"""

import numpy as  np
import cv2

# load the image to detect, get width, height 

img_to_detect = cv2.imread('img_test/test_sweetpumpkin2.jpg')
img_height = img_to_detect.shape[0]
img_width = img_to_detect.shape[1]

# convert to blob to pass into model
img_blob = cv2.dnn.blobFromImage(img_to_detect, 0.003922, (416, 416), swapRB=True, crop=False)
#recommended by yolo authors, scale factor is 0.003922=1/255, width,height of blob is 320,320
#accepted sizes are 320×320,416×416,608×608. More size means more accuracy but less speed

# only single label 
# class_labels = ['가리비', '가지', '게맛살', '고구마', '고등어', '고추', '고추장', '그린올리브', '김', 
#             '꼬막', '녹색피망', '느타리버섯', '다시마', '단호박', '달걀', '당근', '대파', '두부', '땅콩버터', 
#             '랍스타', '레몬', '로메인상추', '리코타치즈', '마늘', '마요네즈', '만두', '명란젓', '모짜렐라치즈', 
#             '무우', '문어', '물미역', '바게트', '밥', '방울토마토', '배추', '배추김치', '버섯', '버터', '베이글', 
#             '브로콜리', '삶은달걀', '새우', '샐러리', '생크림', '소면', '스파게티면', '양배추', '연근', '와플', 
#             '우유', '잡곡식빵', '적양배추', '전복', '체다치즈', '치커리', '칠리소스', '케일', '케첩', '토마토', 
#             '토마토파스타소스', '파슬리', '파인애플', '파프리카', '팽이버섯', '표고버섯']


class_labels = ['scallop', 'eggplant', 'crabstick', 'sweetpotato', 'mackerel', 'chili', 'gochujang', 'greenolive', 'koreangim', 
            'cockle', 'greenbellpepper', 'oystermushroom', 'kelp', 'sweetpumpkin', 'egg', 'carrot', 'koreanleek', 'tofu', 
            'peanutbutter', 'lobster', 'lemon', 'romaine', 'ricottacheese', 'garlic', 'mayonnaise', 'dumpling', 'saltedpollackroe', 
            'mozzarellacheese', 'radish', 'octopus', 'seaweed', 'baquette', 'steamedrice', 'cherrytomato', 'napacabbage', 
            'napacabbagekimchi', 'mushroom', 'butter', 'bagel', 'broccoli', 'boiledegg', 'shrimp', 'salary', 'freshcream', 'plainnoodles', 
            'spaghettinoodles', 'cabbage', 'lotusroot', 'waffle', 'milk', 'cerealbread', 'redcabbage', 'earsheel', 'cheddarcheese', 'chicory', 
            'chilisauce', 'kale', 'ketchup', 'tomato', 'tomatopastasauce', 'parsley', 'pineapple', 'paprika', 'enokimushroom', 'shiitakemushroom']

#Declare only a single color
class_colors = ["0,255,0", "255, 0, 0", "0, 0, 255", "255, 200, 0", "0, 255, 255", "255, 0, 255"]
class_colors = [np.array(every_color.split(",")).astype("int") for every_color in class_colors]
class_colors = np.array(class_colors)
class_colors = np.tile(class_colors,(16,1))

# input preprocessed blob into model and pass through the model
# obtain the detection predictions by the model using forward() method
# yolo_model = cv2.dnn.readNetFromDarknet('./yolov4/darknet_master/yolov4-tiny_64_4.cfg', './yolov4/darknet_master/tiny_weights/yolov4-tiny_64_4_best_74000.weights')
# old
yolo_model = cv2.dnn.readNetFromDarknet('./predict_65_classes/yolov4-tiny_65_classes_64_4.cfg', './predict_65_classes/tiny_weights/yolov4-tiny_64_4_best_72_dot_67.weights')


# Get all layers from the yolo network
# Loop and find the last layer (output layer) of the yolo network 
yolo_layers = yolo_model.getLayerNames()
yolo_output_layer = [yolo_layers[yolo_layer - 1] for yolo_layer in yolo_model.getUnconnectedOutLayers()]

# input preprocessed blob into model and pass through the model
yolo_model.setInput(img_blob)
# obtain the detection layers by forwarding through till the output layer
obj_detection_layers = yolo_model.forward(yolo_output_layer)


############## NMS Change 1 ###############
# initialization for non-max suppression (NMS)
# declare list for [class id], [box center, width & height[], [confidences]
class_ids_list = []
boxes_list = []
confidences_list = []
############## NMS Change 1 END ###########


# loop over each of the layer outputs
for object_detection_layer in obj_detection_layers:
	# loop over the detections
    for object_detection in object_detection_layer:
        
        # obj_detections[1 to 4] => will have the two center points, box width and box height
        # obj_detections[5] => will have scores for all objects within bounding box
        all_scores = object_detection[5:]
        predicted_class_id = np.argmax(all_scores)
        prediction_confidence = all_scores[predicted_class_id]
    
        # take only predictions with confidence more than 20%
        if prediction_confidence > 0.20:
            #get the predicted label
            predicted_class_label = class_labels[predicted_class_id]
            #obtain the bounding box co-oridnates for actual image from resized image size
            bounding_box = object_detection[0:4] * np.array([img_width, img_height, img_width, img_height])
            (box_center_x_pt, box_center_y_pt, box_width, box_height) = bounding_box.astype("int")
            start_x_pt = int(box_center_x_pt - (box_width / 2))
            start_y_pt = int(box_center_y_pt - (box_height / 2))
            
            ############## NMS Change 2 ###############
            #save class id, start x, y, width & height, confidences in a list for nms processing
            #make sure to pass confidence as float and width and height as integers
            class_ids_list.append(predicted_class_id)
            confidences_list.append(float(prediction_confidence))
            boxes_list.append([start_x_pt, start_y_pt, int(box_width), int(box_height)])
            ############## NMS Change 2 END ###########
            
############## NMS Change 3 ###############
# Applying the NMS will return only the selected max value ids while suppressing the non maximum (weak) overlapping bounding boxes      
# Non-Maxima Suppression confidence set as 0.5 & max_suppression threhold for NMS as 0.4 (adjust and try for better perfomance)
max_value_ids = cv2.dnn.NMSBoxes(boxes_list, confidences_list, 0.5, 0.4)
predicted_list = []
# loop through the final set of detections remaining after NMS and draw bounding box and write text
for max_valueid in max_value_ids:
    max_class_id = max_valueid
    box = boxes_list[max_class_id]
    start_x_pt = box[0]
    start_y_pt = box[1]
    box_width = box[2]
    box_height = box[3]
    
    #get the predicted class id and label
    predicted_class_id = class_ids_list[max_class_id]
    predicted_class_label = class_labels[predicted_class_id]
    prediction_confidence = confidences_list[max_class_id]
############## NMS Change 3 END ########### 
           
    end_x_pt = start_x_pt + box_width
    end_y_pt = start_y_pt + box_height
    
    #get a random mask color from the numpy array of colors
    box_color = class_colors[predicted_class_id]
    
    #convert the color numpy array as a list and apply to text and box
    box_color = [int(c) for c in box_color]
    predicted_list.append(predicted_class_label)

    # print the prediction in console
    predicted_class_label_msg = "{}: {:.2f}%".format(predicted_class_label, prediction_confidence * 100)
    print("predicted object {}".format(predicted_class_label_msg))
    
    # draw rectangle and text in the image
    cv2.rectangle(img_to_detect, (start_x_pt, start_y_pt), (end_x_pt, end_y_pt), box_color, 1)
    cv2.putText(img_to_detect, predicted_class_label_msg, (start_x_pt, start_y_pt-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, box_color, 1)

predicted_set_list = list(set(predicted_list))
print(predicted_set_list)
resized_img = cv2.resize(img_to_detect, (800, 800))
cv2.imshow("Detection Output", resized_img)
cv2.waitKey()
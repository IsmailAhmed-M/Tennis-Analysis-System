from ultralytics import YOLO
model = YOLO('yolov8x')  # Load model

result = model.track('input_videos/Tennis Video.mp4',conf = 0.2, save = True)  
#print(result)
# # print('boxes:')
# # for box in result[0].boxes:
# #     print(box)


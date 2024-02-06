# import torch
# from PIL import Image
# from pathlib import Path
#
# model = torch.hub.load('ultralytics/yolov5', 'custom', source='C:/Users/USER/Downloads/yolov5-master/best.pt')
#
# img_path = 'C:/Users/USER/Downloads/yolov5-master/Scr_0001.jpg'
# img = Image.open(img_path)
#
# results = model(img)
#
# results.print()
# results.show()
#
# results.save(Path('runs/detect'))
# results.xyxy[0]

# YOLOv5 PyTorch HUB Inference (DetectionModels only)



# import torch
#
# model = torch.hub.load('ultralytics/yolov5', 'C:/Users/USER/Downloads/yolov5-master/best.pt', force_reload=True)  # yolov5n - yolov5x6 or custom
# im = 'C:/Users/USER/Downloads/yolov5-master/Scr_0001.jpg'  # file, Path, PIL.Image, OpenCV, nparray, list
# results = model(im)  # inference
# results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
# results.show()

python detect.py --source 이미지경로 --weights best.pt

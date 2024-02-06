from flask import Flask, request
from inference import scratch_ratio, predict
from concurrent.futures import ProcessPoolExecutor
from PIL import Image
import io
import torch

app = Flask(__name__)


# 등급산출
# 1등급: 흠집 5% 이하
# 2등급: 흠집 10% 이하
# 3등급: 흠집 15% 이하
# 4등급: 흠집 15% 이상
def rank(df):
   if df < 0.05:
       return 100
   elif df < 0.1:
       return 90
   elif df < 0.15:
       return 80
   elif df < 1:
       return 70
   else:
       return 'error'

def load_model():
   model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')
   model.iou = 0.2
   return model

model = load_model()
def test(im):
   result2 = predict(model, im)
   df = result2.pandas().xyxy[0]
   ratio = scratch_ratio(df)
   rank_result = rank(ratio)
   return rank_result

# def is_error(im):
#     df = predict(im).pandas().xyxy[0]
#     if df.loc[df['class'] == 0].empty:
#         return True
#     else:
#         return False


def process_image(image):
   # 이미지를 메모리에서 로드
   im = Image.open(io.BytesIO(image))

   # 등급 계산 및 출력
   return test(im)



@app.route('/rankingCheck', methods=['POST'])
def hello():
   results = []
   if 'images' in request.files:
       images = request.files.getlist('images')
       images_content = [image.read() for image in images]
       with ProcessPoolExecutor() as executor:
           results = list(executor.map(process_image, images_content))  # 처리 후 응답 반환

   result = sum(results) // len(results)

   if result == 100:
       return 'S'
   elif result > 90:
       return 'A'
   elif result > 80:
       return 'B'
   else:
       return 'C'


if __name__ == '__main__':
   app.run('0.0.0.0:1', debug=True)
# import torch
import pathlib

temp = pathlib.PosixPath
pathlib.PosixPath = pathlib.WindowsPath


# def predict(im):
#     # best모델 불러오기
#     model = torch.hub.load('ultralytics/yolov5', 'custom', 'best.pt')
#
#     # 모델 세부 조정
#     model.iou = 0.2
#     # 예측
#     results = model(im)
#     return results


def predict(model, im):
    results = model(im)
    return results

# def scratch_ratio(im):
#     # xyxy좌표 저장
#     df = predict(im).pandas().xyxy[0]
#     # 휴대폰 xyxy좌표
#     phone_df = df.loc[df['class'] == 0]
#     # 휴대폰 면적
#     phone_sum = (phone_df['xmax'] - phone_df['xmin']) * (phone_df['ymax'] - phone_df['ymin'])
#
#     # 흠집 xyxy좌표
#     scratch_df = df.loc[df['class'] == 1]
#     # 흠집 면적
#     scratch_sum = ((scratch_df['xmax'] - scratch_df['xmin']) * (scratch_df['ymax'] - scratch_df['ymin'])).sum()
#     # 파손율 == 흠집/휴대폰 비율
#     final = scratch_sum / phone_sum
#     # 소수점 2자리까지
#     return final[final.index[0]].round(2)

def scratch_ratio(df):
    phone_sum = df.loc[df['class'].isin([0, 3]), ['xmax', 'xmin', 'ymax', 'ymin']]
    phone_sum = ((phone_sum['xmax'] - phone_sum['xmin']) * (phone_sum['ymax'] - phone_sum['ymin'])).sum()
    if (phone_sum == 0):
        return 'error'
    scratch_sum = df.loc[df['class'].isin([1, 2, 4, 5]), ['xmax', 'xmin', 'ymax', 'ymin']]
    scratch_sum = ((scratch_sum['xmax'] - scratch_sum['xmin']) * (scratch_sum['ymax'] - scratch_sum['ymin'])).sum()
    final = scratch_sum / phone_sum
    return final.round(3)
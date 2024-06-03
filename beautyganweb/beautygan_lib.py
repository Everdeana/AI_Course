# 라이브러리 확인
import dlib
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from PIL import Image
from datetime import datetime

# 학습된 모델 불러오기
detector = dlib.get_frontal_face_detector()
# sp = dlib.shape_predictor("./trained/shape_predictor_68_face_landmarks.dat")
sp = dlib.shape_predictor("./trained/shape_predictor_5_face_landmarks.dat")

# Pre-Trained 모델 불러오기
sess = tf.Session()
sess.run(tf.global_variables_initializer())

saver = tf.train.import_meta_graph('./model/model.meta')
saver.restore(sess, tf.train.latest_checkpoint('./model'))
graph = tf.get_default_graph()

# BeautyGAN X, Y, Xs 설정
X = graph.get_tensor_by_name('X:0') # 소스
Y = graph.get_tensor_by_name('Y:0') # 레퍼런스
Xs = graph.get_tensor_by_name('generator/xs:0') # 화장 한 결과값

# 전처리(실수 : -1~1)
def preprocess(img):
    return img.astype(np.float32) / 127.5 - 1.

# 복원(0~255)
def postprocess(img):
    return ((img + 1.) * 127.5).astype(np.uint8)

# 이미지를 넣으면 수평에 맞는 이미지 추출
def face_align(img):
    dets = detector(img, 1)
    
    objs = dlib.full_object_detections()
    
    for detection in dets:
        s = sp(img, detection)
        objs.append(s)
        
    # 얼굴추출
    faces = dlib.get_face_chips(img, objs, size=256, padding=0.35)
    
    return faces

def makeup(src, ref):
    # 원본이미지
    org_img = dlib.load_rgb_image(src)

    # 화장할 레퍼런스 이미지
    ref_img = dlib.load_rgb_image(ref)

    print("이미지 불러오기 정상")

    # 얼굴 추출
    org_face = face_align(org_img)
    ref_face = face_align(ref_img)

    src_img = org_face[0]
    ref_img = ref_face[0]

    print("얼굴 추출 정상")

    # 전처리
    X_img = preprocess(src_img)
    X_img = np.expand_dims(X_img, axis=0)

    Y_img = preprocess(ref_img)
    Y_img = np.expand_dims(Y_img, axis=0)

    print("전처리 정상")

    # GAN동작
    output = sess.run(Xs, feed_dict={
        X: X_img,
        Y: Y_img
    })

    print("결과 정상")

    # 결과 확인
    # 복원
    result_img = postprocess(output[0])
    # 파일로 저장
    saveImg = Image.fromarray(result_img)

    now = datetime.now()
    today = now.strftime('%Y%m%d')

    saveImg.save(f'./media/result/{today}/1_rst.jpg')
    return f'./media/result/{today}/1_rst.jpg'

# 테스트
# src = './media/source/1.jpg'
# ref = './media/ref/1.jpg'
# save = './media/result'
# save_file = makeup(src, ref, save)
# print('화장결과 :', save_file)






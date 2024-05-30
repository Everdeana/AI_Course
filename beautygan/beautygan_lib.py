#!/usr/bin/env python
# coding: utf-8
# get_ipython().system('pip install matplotlib')
# get_ipython().system('pip install tensorflow==1.9')
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
X = graph.get_tensor_by_name('X:0') # source
Y = graph.get_tensor_by_name('Y:0') # reference
Xs = graph.get_tensor_by_name('generator/xs:0') # 화장한 결과값

# 전처리 (실수: `1 ~ 1)
def preprocess(img):
    return img.astype(np.float32) / 127.5 - 1.

# 복원(0 ~ 255)
def postprocess(img):
    return ((img + 1.) * 127.5).astype(np.uint8)

# 얼굴 분리

# 이미지를 넣으면 수평에 맞게 이미지 추출
def face_align(img):
    dets = detector(img, 1)
    
    objs = dlib.full_object_detections()
    
    for detection in dets:
        s = sp(img, detection)
        objs.append(s)
        
    # 얼굴 추출
    faces = dlib.get_face_chips(img, objs, size = 256, padding = 0.35)
    
    return faces


def makeup(src, ref, save): # (원본 이미지, 화장 이미지, 경로)
    '''
    # 서비스 프로그램으로 개발한다면
        Django(백엔드)
            - source image : /media/source/20240530/src1.jpg
            - reference image : /media/ref/ref1.jpg
            - result file : /media/result/20240530/res1.jpg
            - web : http://localhost:8000/media/result/20240530/res1.jpg
        
    '''

    # 얼굴 불러오기
    # 원본 이미지
    org_img = dlib.load_rgb_image('./source/haaland4.jpg')

    # 화장할 이미지
    ref_img = dlib.load_rgb_image('./ref/jisoo1.jpg')

    # 얼굴 추출
    org_face = face_align(org_img)
    ref_face = face_align(ref_img)

    # 얼굴 확인
    fig, axes = plt.subplots(1, 2, figsize = (16, 10))
    axes[0].imshow(org_face[0])
    axes[1].imshow(ref_face[0])

    # # BeautyGAN 가동하기

    src_img = org_face[0]
    ref_img = ref_face[0]

    # 전처리
    X_img = preprocess(src_img)
    X_img = np.expand_dims(X_img, axis=0)#  (1, x, y, 3) # 1개만 넣을 때 옵션에 차원 1개를(1)을 넣어줘야 한다.

    Y_img = preprocess(ref_img)
    Y_img = np.expand_dims(Y_img, axis=0)

    # GAN 동작
    output = sess.run(Xs, feed_dict={X : X_img, Y : Y_img})

    # 결과 확인
    # 복원
    result_img = postprocess(output[0])
    # 파일로 저장
    saveImg = Image.fromarray(result_img)
    
    now = datetime.now()

    today = now.strftime('%Y_%m_%d')
    saveImg.save(f'./media/{today}/1_rst.jpg')

# 테스트
src = './media/source/haaland4.jpg'
ref = './media/ref/jisoo1.jpg'
save = './media/result'
save_file = makeup(src, ref, save)
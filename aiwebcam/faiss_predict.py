# 라이브러리 불러오기
import numpy as np
from PIL import Image
import faiss
import face_recognition

################################################
# labels
################################################

################################################################################################
# 함수 리스트

# 많이 나온 단어 확인
def most_frequent(data):
    count_list=[]

#count를 담을 리스트 변수 설정
    for x in data: 
        count_list.append(data.count(x))

        # append를 사용하여서 크기를 미리 정하지 않고 초기화 가능
    return data[count_list.index(max(count_list))], max(count_list)
################################################################################################

################################################################################################
# 전역변수

# 벡터 DB 불러오기
# 학습 결과
face_index = faiss.read_index('./train/face_20240527.bin')
# 학습 결과 정답
train_labels = np.load('./train/labels.npy')
################################################################################################

def face_detect(img):

    ################################################################################################
    # 얼굴 검출 프로그램
    ################################################################################################

    # 예측하기
    # 얼굴인식
    test_img = face_recognition.load_image_file('test_img/ujy.jpg')
    test_face = face_recognition.face_locations(test_img)
    if len(test_face) != 1:
        return "unknown"

    # 얼굴만 잘라내기(시계방향)
    top, right, bottom, left = test_face[0]
    print(top, right, bottom, left)

    # 범위 확장
    top = top - 20
    right = right + 20
    bottom = bottom + 20
    left = left - 20

    # 얼굴부분만 추출
    face_cut = test_img[top:bottom, left:right]

    pil_img = Image.fromarray(face_cut)
    pil_img.save('./train_res/test.jpg')
    img = face_recognition.load_image_file('./train_res/test.jpg')

    # 인코딩
    test_en = face_recognition.face_encodings(img)[0]

    # 넘파이
    test_en = np.array(test_en, dtype=np.float32).reshape(-1, 128)
    # (128) -> (1, 128)

    # 예측
    distance, result = face_index.search(test_en, k=5)

    # 값검출
    label = [train_labels[i] for i in result[0]]
    print(label)
    print(distance)

    face_rst = most_frequent(label)

    if face_rst[1] < 3:
        return "unknown"
    else:
        print(f"중복값 개수 : {face_rst[1]}/5")
        print("중복값 : ", end="")
        return face_rst[0]

# print(face_detect('./test_img/ujy.jpg')) # 테스트용
# opencv 버전 확인
import cv2
print(cv2.__version__)

# 이미지 불러오기
image = cv2.imread("nesta.jpg", cv2.IMREAD_COLOR)
cv2.imshow("nesta.jpg", image)
cv2.waitKey()
cv2.destroyAllWindows
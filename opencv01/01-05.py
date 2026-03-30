import cv2
import sys


def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_RBUTTONDOWN:
        print("왼쪽 버튼 클릭:", x, y)

# 이미지 불러오기
img = cv2.imread('lena.jpg')

if img is None:
    print("이미지를 찾을 수 없습니다.")
    sys.exit()

#특정 지점의 색상 파악하기
# (y, x) 좌표의 픽셀 값 접근 [B, G, R]
blue = img[100, 100, 0]
green = img[100, 100, 1]
red = img[100, 100, 2]

print(blue, green, red)

# 특정 영역을 검은색으로 칠하기 (ROI 맛보기)
img[:100, :100] = [0, 0, 0]

cv2.imshow('Lena Window', img)  # 윈도우 창 제목, 이미지 객체
cv2.setMouseCallback('Lena Window', mouse_callback)


# 키 입력 대기 (아무 키나 누르면 종료)
cv2.waitKey(0)
cv2.destroyAllWindows()
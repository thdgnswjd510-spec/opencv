import cv2
import numpy as np


image = cv2.imread('coins.jpg')

# 1. 전처리 및 이진화 (동전=흰색, 배경=검정)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
_, binary = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (10,10))
binary_dilated = cv2.dilate(binary, kernel, iterations=1)


# 2. 플러드필 기법 사용
floodfill = binary_dilated.copy()
h, w = floodfill.shape[:2]

mask = np.zeros((h + 2, w + 2), np.uint8)
cv2.floodFill(floodfill, mask, (0, 0), 255)
floodfill_inv = cv2.bitwise_not(floodfill)
coin_mask = binary_dilated | floodfill_inv
coin_mask = cv2.erode(coin_mask, kernel, iterations=1)


# 3. 완성된 마스크로 외곽선 찾기
contours, _ = cv2.findContours(coin_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 4. 노이즈 제거
filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 500]

# 5. 기존 이미지에 외곽선 그리기
result_image = image.copy()
cv2.drawContours(result_image, filtered_contours, -1, (0, 255, 0), 3)

# 6. 개수 세아리기 및 텍스트 표시
text = f"found {len(contours)} coins"
cv2.putText(result_image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

# 결과 출력
cv2.imshow('Mask', coin_mask)
cv2.imshow('Result', result_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
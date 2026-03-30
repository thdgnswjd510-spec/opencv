import cv2
import numpy as np

# 500x500 크기의 하얀색 배경 생성 (255로 채움)
canvas = np.full((500, 500, 3), 255, dtype=np.uint8)

# 질문하신 코드 부분
cv2.line(canvas, (50, 50), (450, 50), (255, 0, 0), 5)          # 파란 선
cv2.rectangle(canvas, (50, 200), (200, 400), (0, 255, 0), -1) # 초록 꽉 찬 사각형
cv2.circle(canvas, (350, 300), 100, (0, 0, 255), 3)           # 빨간 원
cv2.line(canvas, (400, 400), (450, 450), (100, 5, 30), 4)
cv2.line(canvas, (400, 500), (450, 350), (100, 5, 30), 4)

# 결과 출력
cv2.imshow('Canvas Drawing', canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
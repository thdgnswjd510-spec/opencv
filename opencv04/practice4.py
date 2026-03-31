import cv2
import numpy as np

img = cv2.imread('rail.jpg')
h, w = img.shape[:2]

edges = cv2.Canny(cv2.GaussianBlur(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY), (3, 3), 0), 100, 200)

mask = np.zeros_like(edges)
cv2.fillPoly(mask, np.array([[(0, h), (w // 2, h // 2), (w, h)]], np.int32), 255)

lines = cv2.HoughLinesP(cv2.bitwise_and(edges, mask), 1, np.pi / 180, 130, minLineLength=80, maxLineGap=120)
line_img = np.zeros_like(img)

l_pts, r_pts = [], []

if lines is not None:
    for x1, y1, x2, y2 in lines.reshape(-1, 4):
        if x1 == x2: continue
        slope = (y2 - y1) / (x2 - x1)

        if -5.0 < slope < -0.5:
            l_pts.extend([[y1, x1], [y2, x2]])
        elif 0.5 < slope < 5.0:
            r_pts.extend([[y1, x1], [y2, x2]])

y_b, y_t = h, int(h * 0.55)


get_fit = lambda pts: np.polyfit(np.array(pts)[:, 0], np.array(pts)[:, 1], 1) if pts else None
l_fit, r_fit = get_fit(l_pts), get_fit(r_pts)


for fit in filter(lambda f: f is not None, (l_fit, r_fit)):
    cv2.line(line_img, (int(fit[0] * y_b + fit[1]), y_b), (int(fit[0] * y_t + fit[1]), y_t), (0, 255, 0), 4)

if l_fit is not None and r_fit is not None:
    ty = int(h * 0.8)
    cx = int(((l_fit[0] + r_fit[0]) * ty + l_fit[1] + r_fit[1]) // 2)
    cv2.circle(line_img, (cx, ty), 8, (0, 0, 255), -1)

cv2.imshow('img', cv2.addWeighted(img, 1, line_img, 1, 0))
cv2.waitKey(0)
cv2.destroyAllWindows()
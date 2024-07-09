#!/usr/bin/env python3
import cv2
import numpy as np

image_path = '/home/gihoon/catkin_ws/src/lane_detection/scripts/download.jpg' # 이미지 경로를 설정하세요
image = cv2.imread(image_path)

# 이미지 회전
(h, w) = image.shape[:2]
center = (w / 2, h / 2)
M = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated_image = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Rotated Image', rotated_image)

# 이미지 크기 조정
resized_image = cv2.resize(image, (300, 300))
cv2.imshow('Resized Image', resized_image)

# 이미지 기울이기 (Affine Transform)
pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])
M = cv2.getAffineTransform(pts1, pts2)
affine_image = cv2.warpAffine(image, M, (w, h))
cv2.imshow('Affine Transformed Image', affine_image)

# 모든 창을 동시에 닫기 위해 waitKey와 destroyAllWindows를 한 번만 호출
cv2.waitKey(0)
cv2.destroyAllWindows()
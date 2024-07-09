#!/usr/bin/env python3
import cv2
import rospy
import numpy as np

image_path = '/home/gihoon/catkin_ws/src/opencv_example/src/test_image.png' # 이미지 경로를 설정하세요
image = cv2.imread(image_path)

# 1. 원본 이미지 표시
cv2.imshow('Original Image', image)

# 2. 이미지 회색조로 변환
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray_image)

# 3. 에지 검출 (Canny)
edges = cv2.Canny(image, 50, 150)
cv2.imshow('Edges', edges)

# 4. 가우시안 블러 필터 적용
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)
cv2.imshow('Gaussian Blurred Image', blurred_image)

# 5. 윤곽선 검출
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_image = image.copy()
cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
cv2.imshow('Contours', contour_image)


# 6. 객체 인식 (Haar Cascade를 이용한 얼굴 인식)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
faces = face_cascade.detectMultiScale(gray_image, 1.3, 5)
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('Face Detection', image)

#모든 창을 동시에 닫기 위해 waitKey와 destroyAllWindows를 한 번만 호출
cv2.waitKey(0)
cv2.destroyAllWindows()

# # 이미지 저장
output_path = '/home/gihoon/catkin_ws/src/lane_detection/scripts/output.jpg'
cv2.imwrite(output_path, image)

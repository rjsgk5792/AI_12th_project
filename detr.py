# import cv2 as cv
# import numpy as np


# def main():
    
#     cap = cv.VideoCapture('./data/video/cars.mp4')
    
#     bgs = cv.createBackgroundSubtractorKNN(dist2Threshold =500,detectShadows=False)
    
#     while cap.isOpened():
#         ret, frame = cap.read()
        
#         if not ret:
#             break
        
#         frame = cv.resize(frame,None,fx=0.2,fy=0.2,interpolation = cv.INTER_CUBIC)
#         fgmask = bgs.apply(frame)
    
#         cv.imshow('video', frame)
#         cv.imshow('moving', fgmask)
        
#         if cv.waitKey(1) == ord('q'):
#             break
        
#     cap.release()
#     cv.destroyAllWindows()

# if __name__ == "__main__":
#     main()

# -*- coding: utf-8 -*- 
__author__ = 'Kang' 

import cv2 
# 영상의 의미지를 연속적으로 캡쳐할 수 있게 하는 class 
# 영상이 있는 경로 
vidcap = cv2.VideoCapture('C:/Users/rjsgk/section4/yolov4-deepsort/data/video/MOT17-13-FRCNN-raw.webm')   
count = 0 
while(vidcap.isOpened()): 
  ret, image = vidcap.read() # 이미지 사이즈 960x540으로 변경 
  image = cv2.resize(image, (960, 540)) 
  # 30프레임당 하나씩 이미지 추출 
  if(int(vidcap.get(1)) % 30 == 0): 
    print('Saved frame number : ' + str(int(vidcap.get(1)))) 
    # 추출된 이미지가 저장되는 경로 
    cv2.imwrite("C:/Users/rjsgk/section4/yolov4-deepsort/data/video/frame%d.jpg" % count, image) 
    print('Saved frame%d.jpg' % count) 
    count += 1 
    print(count)


vidcap.release()

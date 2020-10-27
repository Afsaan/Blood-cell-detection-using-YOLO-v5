# Yolo-V5 Object Detection on a Custom Dataset

1. Data — Preprocessing (Yolo-v5 Compatible)

> python preprocess1.py

> python preprocess2.py

2. Training

To start the training process, we need to clone the official Yolo-v5’s weights and config files. It’s available https://github.com/ultralytics/yolov5.

> git clone https://github.com/ultralytics/yolov5

> python yolov5/train.py --img 640 --batch 8 --epochs 100 \
    --data bcc.yaml --cfg models/yolov5s.yaml --name BCCM
    
3. Inference

To predict the images in a Folder
> python yolov5/detect.py --source /content/bcc/images/valid/ 
  --weights '/content/drive/My Drive/Machine Learning Projects/YOLO/best_yolov5_BCCM.pt'
  
To predict a single image file
> output = !python yolov5/detect.py --source /content/bcc/images/valid/BloodImage_00000.jpg 
  --weights '/content/drive/My Drive/Machine Learning Projects/YOLO/best_yolov5_BCCM.pt'

import cv2
import torch
from ultralytics import YOLO

class VLMPerception:
    def __init__(self, model_path="yolov8n.pt"):
        self.model = YOLO(model_path)  # Use a custom-trained model for GUI elements

    def detect_elements(self, image_path):
        image = cv2.imread(image_path)
        results = self.model(image)
        elements = []
        for box in results[0].boxes:
            bbox = box.xyxy[0].cpu().numpy().astype(int).tolist()
            label = self.model.names[int(box.cls[0])]
            elements.append({"bbox": bbox, "label": label})
        return elements

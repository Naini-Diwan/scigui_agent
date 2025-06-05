import cv2

class VLMPerception:
    def __init__(self):
        pass  # Placeholder for model loading

    def detect_elements(self, image_path, instruction):
        # Placeholder: In practice, use a vision-language model like ShowUI
        # Here, we simulate detected elements for demonstration
        return [
            {"bbox": [120, 80, 220, 130], "label": "Open File Button"},
            {"bbox": [300, 400, 500, 420], "label": "Timeline Slider"}
        ]

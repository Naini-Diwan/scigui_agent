FROM python:3.10-slim

RUN pip install torch==2.0.1 opencv-python==4.9.0.80 ultralytics==8.1.0 pyautogui==0.9.54 appium-python-client==3.1.0 selenium==4.18.0 mlflow==2.10.1 dvc==3.50.0 autogen langflow

WORKDIR /workspace
COPY . /workspace

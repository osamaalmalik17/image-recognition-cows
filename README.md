Automated Livestock Monitoring: YOLO-Based Cow Behavior Detection
An automated computer vision pipeline designed to track, classify, and analyze cow behaviors in real-time. By leveraging a custom-trained YOLO model, this project provides actionable insights into livestock welfare, grazing efficiency, and early health anomaly detection. 
Note that this is a project in progress and work is continuously carried out to improve the metrics shown below.
Project Demo: https://github.com/osamaalmalik17/image-recognition-cows/tree/cd603e2cf1f37fdf1ea4b574e27f52d80a29d876/demo
________________________________________
Project Overview
Manual observation of livestock behavior is time-consuming and labor-intensive. This project automates the process by detecting key cow behaviors directly from video streams and image data. 
Key Capabilities:
•	Behavior Classification: Detects specific poses and activities including Grazing, Lying, Standing, Walking. 
•	Automated Logging: Converts visual detections into structured behavioral datasets for trend analysis. 
•	Farm Edge Compatibility: Lightweight model weights optimized for fast inference. ________________________________________
Dataset & Training
Video recordings from cattle farm environments with different angels were analyzed. The annotation process was carried out using software available at https://www.cvat.ai/. Afterwards images and annotations were downloaded to be analyzed using a script based on the Ultralytics YOLO framework and run in PyCharm.
•	Data Split: [74.2%] Training, [25,8%] Validation. 
•	Annotations: Bounding boxes labeled precisely around individual cows with associated behavior classes. 
Model Performance Metrics
The model was trained using the Ultralytics YOLO framework. Below are the finalized metrics from the validation set and the confusion matrix: 

Metric	Value
Epoch Chosen:   	
Best Epoch (Epoch 29 of 50)
mAP50	46.6%
mAP50-95	33.8%
Precision	47.7%
Recall	46.5%
	
 
________________________________________
🚀 Quick Start & Inference
Follow these steps to run the trained model on your own local images or video streams. 
1. Clone the Repository
bash
git clone https://github.com/osamaalmalik17/image-recognition-cows
cd /image-recognition-cows
2. Install Dependencies
bash
pip install ultralytics opencv-python pandas
3. Run a Test Script
Create a Python file (e.g., predict.py) or use the snippet below to execute inference using the stored weights: 
python
from ultralytics import YOLO

# Load the custom trained weights from the repo
model = YOLO("https://github.com/osamaalmalik17/image-recognition-cows/tree/main/cows/runs/detect/train59/weights/best.pt")

# Run inference on an unseen image
results = model("path/to/new_cow_image.jpg", save=True, conf=0.5)

print("Inference complete! Saved results to the 'runs/detect' directory.")
________________________________________
🛠️ Future Roadmap
•	[ ] Deploy a live web dashboard application using Streamlit. 
•	[ ] Integrate ByteTrack for persistent multi-object cow tracking over time. 
•	[ ] Implement an alert system for anomalous behaviors (e.g., prolonged lying down). 
________________________________________
📜 License
Distributed under the MIT License. See LICENSE for more information. 


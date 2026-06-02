from ultralytics import YOLO
model = YOLO("yolo11n.pt")
model.train(
     data=r"C:/Users/AO/Desktop/cows/cows.yaml",
     epochs=50,
     imgsz=640,
     batch=-1,
     mixup=0.5)

from ultralytics import YOLO

# Load your trained model
model = YOLO('C:/Users/AO/Desktop/cows/runs/detect/train59/weights/best.pt')

# Run validation
results = model.val()

# Print the raw confusion matrix (NumPy array)
print(results.confusion_matrix.matrix)




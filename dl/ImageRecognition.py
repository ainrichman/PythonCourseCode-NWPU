from torchvision.io import read_image
from torchvision.models.mobilenetv2 import mobilenet_v2, MobileNet_V2_Weights

img = read_image("cat.jpg")
model = mobilenet_v2(weights="IMAGENET1K_V1")
weights = MobileNet_V2_Weights.DEFAULT
model.eval()
preprocess = weights.transforms()
batch = preprocess(img).unsqueeze(0)
prediction = model(batch).squeeze(0).softmax(0)
class_id = prediction.argmax().item()
score = prediction[class_id].item()
category_name = weights.meta["categories"][class_id]
print(f"{category_name}: {100 * score:.1f}%")

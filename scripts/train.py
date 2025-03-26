import torch
import torchvision.models as models
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
import os

# Hyperparameter
num_epochs = 5
batch_size = 32
learning_rate = 0.001
num_classes = 4  # Renaissance, Baroque, Impressionism, Modern Art

# Modell laden und anpassen
model = models.resnet50(weights=models.ResNet50_Weights.DEFAULT)
model.fc = torch.nn.Linear(model.fc.in_features, 4)

# Transformationen
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
])

# Dataset und DataLoader
dataset = ImageFolder(root="data", transform=transform)
loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Optimierer und Verlustfunktion
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)
criterion = torch.nn.CrossEntropyLoss()

# Modelltraining
print("🚀 Training gestartet...")
model.train()
for epoch in range(num_epochs):
    epoch_loss = 0.0
    for images, labels in loader:
        outputs = model(images)
        loss = criterion(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        epoch_loss += loss.item()
    print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {epoch_loss/len(loader):.4f}")

# Modell speichern
os.makedirs("models", exist_ok=True)
torch.save(model.state_dict(), "models/art_style_model.pth")
print("✅ Modell erfolgreich gespeichert!")
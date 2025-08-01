# import zipfile
# zip_ref=zipfile.ZipFile("archive (28).zip")
# zip_ref.extractall()
# zip_ref.close()

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import numpy as np
from tensorflow.keras.preprocessing import image
import os

# Paths & configs
data_dir = "garbage-dataset"
img_size = (224, 224)
batch_size = 32
epochs = 15  # Increase for better results

# Data generators
datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

train_generator = datagen.flow_from_directory(
    data_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='training'
)

val_generator = datagen.flow_from_directory(
    data_dir,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Load MobileNetV2 base model
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
# Fine-tune the top 50 layers
for layer in base_model.layers[-50:]:
    layer.trainable = True

# Classification head
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.3)(x)
x = Dense(256, activation='relu')(x)
output = Dense(train_generator.num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=output)

# # Compile model
# model.compile(optimizer=Adam(learning_rate=0.0001),
#               loss='categorical_crossentropy',
#               metrics=['accuracy'])

# # Train
# history = model.fit(
#     train_generator,
#     validation_data=val_generator,
#     epochs=epochs
# )

# # Save
# model.save("Waste_classifier_v2.h5")

# Show class indices for verification
print("\n📚 Class Indices:")
for cls, idx in train_generator.class_indices.items():
    print(f"{idx}: {cls}")

# Load image for prediction
img_path = "garbage-dataset/clothes/clothes_10.jpg"
img = image.load_img(img_path, target_size=img_size)
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Predict
pred = model.predict(img_array)
pred_class_idx = np.argmax(pred)
confidence = np.max(pred)

# Get readable class name
class_labels = list(train_generator.class_indices.keys())
predicted_class = class_labels[pred_class_idx]

# Output
print(f"\n🧠 Predicted class: {predicted_class}")
print(f"✅ Confidence: {confidence * 100:.2f}%")




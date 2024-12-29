from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st

def teachable_machine_classification(img):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_Model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Ensure the image is in RGB format and resize it
    size = (224, 224)
    img = img.convert("RGB")  # Convert to RGB
    img = ImageOps.fit(img, size, Image.Resampling.LANCZOS)

    # Turn the image into a numpy array
    image_array = np.asarray(img)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predict using the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()  # Strip newlines and spaces
    confidence_score = prediction[0][index]

    return class_name, confidence_score

def main():
    st.title("Image Classification With Google's Teachable Machine")
    st.header("Brain Tumor MRI Classification")
    st.text("Upload a Brain MRI Image for Classification as Tumor or No-Tumor")

    # File uploader for image
    uploaded_file = st.file_uploader("Choose a Brain MRI...", type=["jpg", "png", "jpeg"])
    if uploaded_file is not None:
        # Open the image
        image_file = Image.open(uploaded_file)
        st.image(image_file, caption="Uploaded MRI Image", use_column_width=True)

        # Run classification
        st.write("")
        st.write("Classifying the image...")
        label, confidence_score = teachable_machine_classification(image_file)

        # Display the results
        if label == "1 Yes":  # Adjust label comparison based on your labels.txt content
            st.error(f"MRI Scan shows a Brain Tumor. Confidence Score: {confidence_score:.2f}")
        else:
            st.success(f"No Brain Tumor detected. Confidence Score: {confidence_score:.2f}")

if __name__ == '__main__':
    main()

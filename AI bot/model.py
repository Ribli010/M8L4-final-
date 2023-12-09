from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np


def get_class(image):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(image).convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)  

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    trash = class_name[2:-1]

    if trash == "Bottle":
        return "Стеклянные бутылки следует выбрасывать в специальные мусорные баки, как и бутылки из пластика, пластик из которых в скором времени попадает на переработку.В 2015 году было проведено исследование ,в котором выяснилось ,что только 20 процентов пластика перерабатывается.К сожалению большинство пластиковых отходов пригодны только для одного цикла переработки ,ибо процесс переработки ухудшиет общую целостность пластика."
    if trash == "Plastic bag":
        return "Пластиковые пакеты желательно сдавать на переработку, как и весь пластик в общем. Некоторые люди используют их так же как мешки для мусора."
    if trash == "Plastic container":
        return "Пластиковые контейнеры для еды можно использовать повторно или выкинуть в специальный мусорный бак для перерабатываемых отходов."
    if trash == "Tin":
        return "Алюминевые/жестяные банки желательно выбрасывать в контейнер для последующей переработки."
import cv2
from PIL import Image

clasificador = 'haarcascade_frontalface_default.xml'

def anonimizacion(output_file, image_to_anonymise):
    try:
        # Cargar la imagen
        image = cv2.imread(image_to_anonymise)

        # Verifica si la imagen fue cargada correctamente
        if image is None:
            raise ValueError("No se pudo cargar la imagen. Verifica que el archivo sea válido.")

        # Convertir la imagen a escala de grises
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Cargar el clasificador de detección de caras desde la ruta de OpenCV
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Verifica si el clasificador se cargó correctamente
        if face_cascade.empty():
            raise IOError("No se pudo cargar el clasificador de detección de caras.")

        # Detectamos caras en la imagen
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
        print(f"Se detectaron {len(faces)} caras.")

        # Verifica si se detectaron caras
        if len(faces) == 0:
            print("No se detectaron caras en la imagen.")
            return Image.open(image_to_anonymise)

        # Procesar cada cara detectada con desenfoque gaussiano
        for (x, y, w, h) in faces:
            face = image[y:y+h, x:x+w]
            blurred_face = cv2.GaussianBlur(face, (99, 99), 30)
            image[y:y+h, x:x+w] = blurred_face

        # Guardar la imagen procesada
        cv2.imwrite(output_file, image)

        # Devolver la imagen procesada
        return Image.open(output_file)

    except Exception as e:
        print(f"Error durante la anonimización: {e}")
        raise

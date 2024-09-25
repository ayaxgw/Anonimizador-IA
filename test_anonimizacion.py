import cv2

clasificador = 'haarcascade_frontalface_default.xml'

image_path ='image_path.jpg'

# cargar la imagen
image = cv2.imread(image_path)

# convertir la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cargamos el clasificador de deteccion de caras
face_cascade = cv2.CascadeClassifier(clasificador)

# detectamos caras en la imgen
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30,30))

# crea rectangulo alrededor de la cara detectada 
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x,y),(x+w, y+h), (0, 255,0),2)

# mostramos la imagen con las caras detectadas
cv2.imshow('Caras detectadas', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

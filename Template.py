import cv2
# test preview

# Función para decodificar el código QR
def decodificar_qr(imagen):
    # Cargamos el detector de códigos QR
    detector_qr = cv2.QRCodeDetector()

    # Detectamos el código QR en la imagen
    datos_qr, puntos_qr, _ = detector_qr.detectAndDecode(imagen)

    return datos_qr

# Función para mostrar la vista previa de la cámara
def mostrar_vista_previa(camara):
    while True:
        # Capturamos la imagen de la cámara
        ret, imagen = camara.read()

        # Mostramos la imagen en pantalla
        cv2.imshow("Vista previa", imagen)

        # Salimos del bucle si se presiona la tecla "q"
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

# Configuramos la cámara
camara = cv2.VideoCapture(0)

# Mostramos la vista previa de la cámara
mostrar_vista_previa(camara)

# Bucle para leer el código QR
while True:
    # Capturamos la imagen de la cámara
    ret, imagen = camara.read()

    # Decodificamos el código QR en la imagen
    datos_qr = decodificar_qr(imagen)

    # Si se encontró un código QR, imprimimos su valor
    if datos_qr:
        print("Valor del código QR:", datos_qr)
        break

# Liberamos la cámara
camara.release()
cv2.destroyAllWindows()

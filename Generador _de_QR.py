import qrcode 
import os

ruta_creacion = os.path.join(os.path.expanduser("~"),"Downloads")

enlace = "https://barelescobar.netlify.app/"
img = qrcode.make(enlace)

nombre_archivo = "qr_bar.png"
ruta_completa = os.path.join(ruta_creacion, nombre_archivo)
img.save(ruta_completa)

print(f"{ruta_completa}")

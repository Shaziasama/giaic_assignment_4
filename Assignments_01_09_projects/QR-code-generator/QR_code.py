#projet 7 QR code generator in python
import qrcode
data = "QR Code Generator"
img = qrcode.make(data)
img.save("QRCode.png")
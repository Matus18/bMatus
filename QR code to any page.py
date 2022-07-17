import pyqrcode
import png

link = '#Here put the link to create a qr' 
qr_code = pyqrcode.create(link)
qr_code.png("Instagram.png", scale =5) #.png create the qr code image

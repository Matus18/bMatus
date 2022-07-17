import pyqrcode
import png

link = 'https://www.instagram.com/yourusername/' #Put your username
qr_code = pyqrcode.create(link)
qr_code.png("Instagram.png", scale =5) #.png create the qr code image

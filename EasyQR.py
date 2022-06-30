#import the pyqrcode module.
import pyqrcode
#imports the pypng module.
import png

# s variable can be anything you desired to be the variable that holds the url
s = 'https://www.advosi.com/'

#This function creates the qr code
url = pyqrcode.create(s)

#This saves the qrcode as a png file on whatever the destination is when ran on cmd or terminal.
#In the parathensis the scale is how big you want the qr image to be.
url.png('advosi.png', scale = 6)


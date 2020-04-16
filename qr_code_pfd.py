#
# LICENSE: free use
#
#Copyright (c) 2018 -- 2020 Ivan Colantoni


#Small architecture to generate PDF qr-code tickets for any kind of uses. Every ticket has inside its own hexa-decimal code
# plus further optional information. I distinguish two different folders ( FOLDER_A and FOLDER_B) in order to give the possibility 
# of generating two different kind of tickets for the same event. In the folder archive are stored all the 
#generated tickets with the distinction I made above. It's used for practical checking in case of errors or claiming.
# In the file CODE_LIST are stored all the hexa-code generated in the pipeine. You don't have to update it, and it's strongly reccomended 
#to NOT modify it. Moreover in the case you want to add other informations inside the qr-code you have to manually modify the files 'NamesA' or 'NamesB'.
#to each line of the file correspond the information stored in one ticket. Remember to cancel all previous insertion of the file any time you make a run or
#you will regenerate the same tickets (e.g. you have to start from line 1 every time). The qrcodes are printed over a picture that you can choose for FOLDER_A and FOLDERB
# and saved as sample.jpeg in the corresponding folder. Any time you make a run the CODE_LIST is updated, your tickets are stored in tickets/FOLDER_A or B. you can check it and 
#then manually move it to the archive once you're sure you made it right. Remember to change path to folders in the code.


import qrcode 
import secrets 
from PIL import Image 
import os
import cv2 
import fpdf
import sys 


with open('CODE_LIST') as f:
   count = sum(1 for _ in f)

print(count)
f = open("CODE_LIST","a")

qr_open={}
img={}	

path1 = '/path/to/tickets/FOLDER_A'
path2 = '/path/to/tickets/FOLDER_B'


## FOLDER A
if sys.argv[2] == "A":
	os.chdir(path1)
	if sys.argv[3] == 'N':
		with open ('NamesA','r') as n:
			list_name = [line for line in n.readlines()]
			print(list_name)
		for i in range(count + 1, count + int(sys.argv[1])+1):
			pdf = fpdf.FPDF('P','mm','A4')
			pdf.add_page()
			pdf.set_fill_color( 67, 187, 70)
			qr_open = qrcode.QRCode(
				version=1,
				error_correction=qrcode.constants.ERROR_CORRECT_H,
				box_size=5,
				border=1,
				)
			code = secrets.token_hex(6)
			f.write(code+ "\n")
			qr_open.add_data(code +"%Folder_A%")
			img = qr_open.make_image(fill_color="black", back_color="white")

			width, height = img.size
			img.save("QR"+ str(i) + ".png")
			width ,height = img.size
			pdf.set_margins( 0.0, 0.0, 0.0)
			pdf.image("sample.jpeg",x=-25,y=-10, w=254, h=318)
			pdf.image("QR"+ str(i) + ".png", x = 55, y = 95, w = width*3/5, h = height*3/5)
			pdf.set_font('Courier','', 24)
			pdf.set_text_color(200,200,200);
			pdf.set_y(270)
			pdf.cell(200,1, code ,0,1,'C')
			pdf.output(list_name[i-(count +1 )])
			print(sys.argv[0] + "Folder_A" + str(i))
	else : 
		for i in range(count + 1, count + int(sys.argv[1])+1):
			pdf = fpdf.FPDF('P','mm','A4')
			pdf.add_page()
			qr_open = qrcode.QRCode(
				version=1,
				error_correction=qrcode.constants.ERROR_CORRECT_H,
				box_size=5,
				border=1,
				)
			code = secrets.token_hex(6)
			f.write(code+ "\n")
			qr_open.add_data(code +"%Folder A%")
			qr_open.make(fit=True)	
			img = qr_open.make_image(fill_color="black", back_color="white")

			width, height = img.size
			img.save("QR"+ str(i) + ".png")
			width ,height = img.size
			pdf.set_margins( 0.0, 0.0, 0.0)
			pdf.image("sample.jpeg",x=-25,y=-10, w=254, h=318)
			pdf.set_font('Courier','', 24)
			pdf.set_text_color(200,200,200);
			pdf.set_y(270)
			pdf.cell(200,1, code ,0,1,'C')
			pdf.image("QR"+ str(i) + ".png", x = 55, y = 95, w = width*3/5, h = height*3/5)
			pdf.output("QR_OP"+ str(i)+".pdf" ,'F')
			print(sys.argv[0] + "Folder_A" + str(i))
for file in os.listdir(path1):
	if file.endswith('.png'):
		os.remove(file) 


#FOLDER_B
os.chdir('path/to/qrcode')
if sys.argv[2] == "B":
	os.chdir(path2)
	if sys.argv[3] == 'N':
		with open ('NamesB','r') as n:
			list_name = [line for line in n.readlines()]
			print(len(list_name))
			for i in range(count + 1, count + int(sys.argv[1])+1):
						pdf = fpdf.FPDF('P','mm','A4')
						pdf.add_page()
						pdf.set_fill_color( 67, 187, 70)
						qr_open = qrcode.QRCode(
							version=1,
							error_correction=qrcode.constants.ERROR_CORRECT_H,
							box_size=5,
							border=1,
							)
						code = secrets.token_hex(6)
						f.write(code+ "\n")
						qr_open.add_data(code +"%Folder B%")
						img = qr_open.make_image(fill_color="black", back_color="white")
						width, height = img.size
						img.save("QR"+ str(i) + ".png")
						width ,height = img.size
						pdf.set_margins( 0.0, 0.0, 0.0)
						pdf.image("sample.jpeg",x=-25,y=-10, w=254, h=318)
						pdf.image("QR"+ str(i) + ".png", x = 55, y = 95, w = width*3/5, h = height*3/5)
						pdf.set_font('Courier','', 24)
						pdf.set_text_color(200,200,200);
						pdf.set_y(270)
						pdf.cell(200,1, code ,0,1,'C')
						pdf.output(list_name[i-(count +1)])
						print(sys.argv[0] + "Folder_B" + str(i))
	else : 
			for i in range(count + 1, count + int(sys.argv[1])+1):
				pdf = fpdf.FPDF('P','mm','A4')
				pdf.add_page()
				qr_open = qrcode.QRCode(
					version=1,
					error_correction=qrcode.constants.ERROR_CORRECT_H,
					box_size=5,
					border=1,
					)
				code = secrets.token_hex(6)
				f.write(code+ "\n")
				qr_open.add_data(code +"%Folder B ")
				qr_open.make(fit=True)	
				img = qr_open.make_image(fill_color="black", back_color="white")

				width, height = img.size
				img.save("QR"+ str(i) + ".png")
				width ,height = img.size
				pdf.set_margins( 0.0, 0.0, 0.0)
				pdf.image("sample.jpeg",x=-25,y=-10, w=254, h=318)
				pdf.set_font('Courier','', 24)
				pdf.set_text_color(200,200,200);
				pdf.set_y(270)
				pdf.cell(200,1, code ,0,1,'C')
				pdf.image("QR"+ str(i) + ".png", x = 55, y = 95, w = width*3/5, h = height*3/5)
				pdf.output("QR_TI"+ str(i)+".pdf" ,'F')
				print(sys.argv[0] + "Folder_B" + str(i))

for file in os.listdir(path2):
	if file.endswith('.png'):
		os.remove(file) 

os.chdir('/path/to/qrcode')


# THE CODE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE CODE OR THE USE OR OTHER DEALINGS IN THE
# CODE.
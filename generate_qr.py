import qrcode


#Your IP address and port
url = "https://gulshankr.pythonanywhere.com"
url ="http://127.0.0.1:5000"


#Generate QR Code
qr = qrcode.make(url)

#Save QR Code as image
qr.save("student_result_qr.png")

print("QR Code generated successfully!")
print("File saved as : student_result_qr .png")
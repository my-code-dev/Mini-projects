import qrcode 
qr = qrcode.QRCode(version=1, box_size=10, border=5)
wifi = "WIFI:S:MyWifi;T:WPA;P:MYPASSWORD123;;"
qr.add_data(wifi)
qr.make(fit=True)
img = qr.make_image(fill_color="black", black_color="white")
img.save("qr_code_wifi.png")
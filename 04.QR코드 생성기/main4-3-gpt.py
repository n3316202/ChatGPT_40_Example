import qrcode
from PIL import Image
import os

# "04.QR 코드 생성기" 폴더 생성
output_folder = "04.QR 코드 생성기"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# "qrdata.txt" 파일에서 데이터 읽기
data_file = os.path.join(output_folder, "qrdata.txt")
default_data = ["데이터1", "데이터2", "데이터3"]

if os.path.exists(data_file):
    with open(data_file, "r") as file:
        data = file.read().splitlines()
else:
    data = default_data

# 각 데이터에 대한 QR 코드 생성 및 이미지 저장
for i, text in enumerate(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img_path = os.path.join(output_folder, f"qr_code_{i + 1}.png")
    img.save(img_path)

    print(f"QR 코드 이미지 {i + 1}가 {img_path}에 저장되었습니다.")
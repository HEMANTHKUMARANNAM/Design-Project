import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Example usage
# text_data = "Lay's Classic Potato Chips (about 28 grams)\nCalories: Around 160\nTotal Fat: Approximately 10 grams\n\nSaturated Fat: About 1.5 grams\nTrans Fat: Usually 0 grams"
# Cholesterol: Typically 0 milligrams
# Sodium: Roughly 170 milligrams
# Total Carbohydrates: Around 15 grams
# Dietary Fiber: Usually less than 1 gram
# Sugars: Typically 0 grams
# Protein: Approximately 2 grams"

text_data = "GOODDAY,SNACKS,2025-12-08"


filename = "qr_code.png"
generate_qr_code(text_data, filename)
print(f"QR Code generated and saved as '{filename}'")

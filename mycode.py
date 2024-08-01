# import qrcode

# def generate_qr_code(data, filename):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(data)
#     qr.make(fit=True)

#     img = qr.make_image(fill_color="black", back_color="white")
#     img.save(filename)



# text_data = "GOODDAY,SNACKS,2027-11-18,www.britannia.co.in/_next/image?url=https%3A%2F%2Fmedia.britannia.co.in%2FGood_Day_Butter_3fe296d24b.jpg&w=1920&q=100@Producer$ Britannia Industries Limited;Origin$ Bangalore? Karnataka? India;Certifications$ FSSAI? ISO 22000;Ingredients$ ;Wheat flour? sugar? edible vegetable oil? butter? invert syrup? leavening agents (ammonium bicarbonate? sodium bicarbonate)? salt? milk solids? emulsifiers (soya lecithin)? artificial flavor (butter);Nutrition Facts (per 100g serving)$;Energy$ 502 kcal;Protein$ 7g;Fat$ 26g;Carbohydrates$ 61g;Dietary Fiber$ 1g;Sugar$ 22g;Sodium$ 374mg#meow"

# filename = "qr_code.png"
# generate_qr_code(text_data, filename)
# print(f"QR Code generated and saved as '{filename}'")


# import qrcode

# def generate_qr_code(data, filename):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_L,
#         box_size=10,
#         border=4,
#     )
#     qr.add_data(data)
#     qr.make(fit=True)

#     img = qr.make_image(fill_color="black", back_color="white")
#     img.save(filename)

# # Example usage
# # text_data = "Lay's Classic Potato Chips (about 28 grams)\nCalories: Around 160\nTotal Fat: Approximately 10 grams\n\nSaturated Fat: About 1.5 grams\nTrans Fat: Usually 0 grams"
# # Cholesterol: Typically 0 milligrams
# # Sodium: Roughly 170 milligrams
# # Total Carbohydrates: Around 15 grams
# # Dietary Fiber: Usually less than 1 gram
# # Sugars: Typically 0 grams
# # Protein: Approximately 2 grams"

# text_data = "Frooti,Cool Drink,2025-11-08,m.media-amazon.com/images/I/41waTyFgWDL._SX300_SY300_QL70_FMwebp_.jpg@Producer$ Parle Agro Pvt Ltd;Origin$ Mumbai? Maharashtra? India ;Certifications$ FSSAI? ISO 22000 ;Ingredients$ Water? mango pulp (19.5%)? sugar? acidity regulator (citric acid)? antioxidant (ascorbic acid)? permitted class II preservative (potassium sorbate) ;Nutrition Facts (per 100ml serving)$;Energy$ 65 kcal;Protein$ 0g;Fat$ 0g;Carbohydrates$ 16.1g;Sugar$ 15g;Sodium$ 10mg#meow"

# filename = "qr_code.png"
# generate_qr_code(text_data, filename)
# print(f"QR Code generated and saved as '{filename}'")






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

text_data = "Maggi,Cool Drink,2027-11-08,5.imimg.com/data5/SELLER/Default/2022/7/MU/PJ/SD/5742893/maggi-noodles-1000x1000.jpg@Producer$ Nestlé India Origin$ India ;Certifications$ FSSAI? ISO 9001? ISO 22000;Ingredients$;Noodles$ ;Wheat flour? edible vegetable oil (palm oil)? salt? mineral (calcium carbonate)? wheat gluten? mineral (magnesium carbonate)? guar gum? raising agent (500(ii))?emulsifier (322? derived from soya)? acidity regulator (500(i))? thickener (412);Nutrition Facts (per 100g serving)$;Energy$ 448 kcal;Protein$ 9g;Fat$ 19g;Carbohydrates$ 60g;Dietary Fiber$ 2.6g;Sugar$ 0.7g;Sodium$ 1040mg#meow"

filename = "qr_code.png"
generate_qr_code(text_data, filename)
print(f"QR Code generated and saved as '{filename}'")
url = input("Lütfen URL haline getirmek istediğiniz metni yapıştırınız:")

smaller = url.lower()

charChenger= smaller.replace(" ","-")
output = charChenger.replace("ü", "u").replace("ı", "i").replace("ğ", "g").replace("ş", "s").replace("ç", "c").replace("ö", "o")
print(output)

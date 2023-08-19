import random
import string

def generate_id():
    letters = ''.join(random.choices(string.ascii_letters, k=2))
    digits = ''.join(random.choices(string.digits, k=2))
    return f"{letters}{digits}{letters}"

def generate_data():
    isim = ''.join(random.choices(string.ascii_letters, k=10))
    soyisim = ''.join(random.choices(string.ascii_letters, k=10))
    tc = ''.join(random.choices(string.digits, k=11))
    brans = random.choice(["Yapay Zeka", "Coğrafya", "Mühendislik", "Tıp", "Edebiyat"])
    maas = random.randint(15000, 50000)
    telefon = ''.join(random.choices(string.digits, k=10))
    id = generate_id()
    return f"İsim: {isim}, Soyisim: {soyisim}, TC: {tc}, Branş: {brans}, Maaş: {maas}, Telefon Numarası: {telefon}, ID: {id}\n"

def main():
    with open("bilgiler.txt", "w", encoding="utf-8") as file:
        for _ in range(50):
            data = generate_data()
            file.write(data)

if __name__ == "__main__":
    main()
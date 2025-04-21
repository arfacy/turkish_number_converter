import re

def text_to_number(text):
    birler = {
        "bir": 1, "iki": 2, "üç": 3, "dört": 4, "beş": 5,
        "altı": 6, "yedi": 7, "sekiz": 8, "dokuz": 9, "sıfır": 0
    }
    onlar = {
        "on": 10, "yirmi": 20, "otuz": 30, "kırk": 40,
        "elli": 50, "altmış": 60, "yetmiş": 70,
        "seksen": 80, "doksan": 90
    }

    def parse_number(words):
        total = 0
        current = 0
        for word in words:
            if word in birler:
                current += birler[word]
            elif word in onlar:
                current += onlar[word]
            elif word == "yüz":
                if current == 0:
                    current = 100
                else:
                    current *= 100
            elif word == "bin":
                if current == 0:
                    current = 1000
                else:
                    current *= 1000
                total += current
                current = 0
        return str(total + current)

    def replace_number_words(match):
        kelimeler = match.group(0).split()
        return parse_number(kelimeler)

    # ✔️ Tüm ardışık sayı kelimelerini eşle
    pattern = r"\b(?:sıfır|bir|iki|üç|dört|beş|altı|yedi|sekiz|dokuz|on|yirmi|otuz|kırk|elli|altmış|yetmiş|seksen|doksan|yüz|bin)(?:\s+(?:sıfır|bir|iki|üç|dört|beş|altı|yedi|sekiz|dokuz|on|yirmi|otuz|kırk|elli|altmış|yetmiş|seksen|doksan|yüz|bin))*\b"

    return re.sub(pattern, replace_number_words, text)




# import re

# def text_to_number(text):
#     birler = {
#         "bir": 1, "iki": 2, "üç": 3, "dört": 4, "beş": 5,
#         "altı": 6, "yedi": 7, "sekiz": 8, "dokuz": 9, "sıfır": 0
#     }
#     onlar = {
#         "on": 10, "yirmi": 20, "otuz": 30, "kırk": 40,
#         "elli": 50, "altmış": 60, "yetmiş": 70,
#         "seksen": 80, "doksan": 90
#     }

#     def parse_number(words):
#         total = 0
#         current = 0
#         for word in words:
#             if word in birler:
#                 current += birler[word]
#             elif word in onlar:
#                 current += onlar[word]
#             elif word == "yüz":
#                 if current == 0:
#                     current = 100
#                 else:
#                     current *= 100
#             elif word == "bin":
#                 if current == 0:
#                     current = 1000
#                 else:
#                     current *= 1000
#                 total += current
#                 current = 0
#         return str(total + current)

#     def replace_number_words(match):
#         kelimeler = match.group(0).split()
#         return parse_number(kelimeler)

#     pattern = r"(sıfır|bir|iki|üç|dört|beş|altı|yedi|sekiz|dokuz|on|yirmi|otuz|kırk|elli|altmış|yetmiş|seksen|doksan|yüz|bin)(\\s+(bir|iki|üç|dört|beş|altı|yedi|sekiz|dokuz))?"

#     return re.sub(pattern, replace_number_words, text)




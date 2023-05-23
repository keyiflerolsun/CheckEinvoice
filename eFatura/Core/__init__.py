# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from ..Libs.Oturum import legacy_session
from shutil        import copyfileobj
from uuid          import uuid4
from os            import remove
from PIL           import Image
from pytesseract   import image_to_string

def e_fatura(vergi_numarasi:str) -> bool:
    """Vergi veya TC Kimlik Numarasından E-Fatura Mükellefiyet Sorgusu"""
    captcha_resmi = f"captcha_{uuid4()}.jpg"

    while True:
        oturum = legacy_session()
        oturum.headers.update({
            "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
        })

        captcha_istek = oturum.get("https://sorgu.efatura.gov.tr/kullanicilar/img.php", stream=True)
        with open(captcha_resmi, "wb") as dosya:
            copyfileobj(captcha_istek.raw, dosya)

        captcha_metni = image_to_string(Image.open(captcha_resmi)).strip()
        remove(captcha_resmi)

        e_fatura_istek = oturum.post(
            url  = "https://sorgu.efatura.gov.tr/kullanicilar/xliste.php",
            data = {"search_string": f"{vergi_numarasi}", "captcha_code": f"{captcha_metni}", "submit": "Ara"}
        )
        if "Güvenlik kodu hatalı" in e_fatura_istek.text:
            continue

        return "Mükellef kayıtlıdır" in e_fatura_istek.text
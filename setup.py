# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from setuptools import setup
from io         import open

setup(
    # ? Genel Bilgiler
    name         = "eFatura",
    version      = "1.0.1",
    url          = "https://github.com/keyiflerolsun/E-Fatura_Sorgu",
    description  = "Vergi veya TC Kimlik Numarasından E-Fatura Mükellefiyet Sorgusu",
    keywords     = ["eFatura", "KekikAkademi", "keyiflerolsun"],

    author       = "keyiflerolsun",
    author_email = "keyiflerolsun@gmail.com",

    license      = "GPLv3+",
    classifiers  = [
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Programming Language :: Python :: 3"
    ],

    # ? Paket Bilgileri
    packages         = ["eFatura"],
    python_requires  = ">=3.10",
    install_requires = [
        "setuptools",
        "wheel",
        "Kekik",
        "requests",
        "urllib3",
        "Pillow",
        "pytesseract"
    ],

    # ? Konsoldan Çalıştırılabilir
    entry_points = {
        "console_scripts": [
            "eFatura = eFatura.konsol:basla",
        ]
    },

    # ? PyPI Bilgileri
    long_description_content_type = "text/markdown",
    long_description              = "".join(open("README.md", encoding="utf-8").readlines()),
    include_package_data          = True
)
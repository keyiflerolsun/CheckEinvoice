# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from eFatura.KekikGUI import KekikGUI
import os

ust_dizin_ver = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])

def dosya_ver(dosya_yolu:str, ust_dizin:int):
    return os.path.join(ust_dizin_ver(__file__, ust_dizin), dosya_yolu)

def basla():
    arayuz = KekikGUI(logo_yolu=dosya_ver("logo.png", 1))
    arayuz.goster()
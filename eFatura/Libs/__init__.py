# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from rich.console import Console
konsol = Console(log_path=False)

import os

ust_dizin_ver = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])

def dosya_ver(dosya_yolu:str, ust_dizin:int):
    return os.path.join(ust_dizin_ver(__file__, ust_dizin), dosya_yolu)
# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from .Libs   import konsol
from eFatura import e_fatura
from sys     import argv

def basla():
    print()

    if len(argv) != 2:
        konsol.print("[bold yellow2][!] Lütfen Vergi Numarası veya TC Kimlik Numarası Belirtin..")
        konsol.print("\n[turquoise2]Örn.: [pale_green1]eFatura 11111111111\n")
        return

    if e_fatura(argv[1]):
        konsol.print(f"[green][+] [light_coral]{argv[1]}[/] Numarası E-Fatura Mükellefidir..\n")
    else:
        konsol.print(f"[red][~] [light_coral]{argv[1]}[/] Numarası E-Fatura Mükellefi Değildir..\n")

if __name__ == "__main__":
    basla()
# 🔍 eFatura

![Repo Boyutu](https://img.shields.io/github/repo-size/keyiflerolsun/eFatura?logo=git&logoColor=white)
![Görüntülenme](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https://github.com/keyiflerolsun/eFatura&title=Görüntülenme)
<a href="https://KekikAkademi.org/Kahve" target="_blank"><img src="https://img.shields.io/badge/☕️-Kahve Ismarla-ffdd00" title="☕️ Kahve Ismarla" style="padding-left:5px;"></a>

![Python Version](https://img.shields.io/pypi/pyversions/eFatura?logo=python&logoColor=white)
![License](https://img.shields.io/pypi/l/eFatura?logo=gnu&logoColor=white)
![Status](https://img.shields.io/pypi/status/eFatura?logo=windowsterminal&logoColor=white)

[![PyPI](https://img.shields.io/pypi/v/eFatura?logo=pypi&logoColor=white)](https://pypi.org/project/eFatura)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/eFatura?logo=pypi&logoColor=white)](https://pypi.org/project/eFatura)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/eFatura?logo=pypi&logoColor=white)](https://pypi.org/project/eFatura)

[![Fonksiyon Testleri ve PyPI Yükle](https://github.com/keyiflerolsun/eFatura/actions/workflows/KekikFlow.yml/badge.svg)](https://github.com/keyiflerolsun/eFatura/actions/workflows/KekikFlow.yml)

*Vergi veya TC Kimlik Numarasından E-Fatura Mükellefiyet Sorgusu*

![eFatura](https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/SS.png)

[![ForTheBadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](https://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/keyiflerolsun/)

## 🚀 Kurulum

### <img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/pypi.svg"> PyPi (Lib - CLI - UI)

```bash
# Yüklemek
pip install eFatura

# Güncellemek
pip install -U eFatura
```

## 📝 Kullanım

### <img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/python.svg"> Lib

```python
from eFatura import e_fatura

print(e_fatura("11111111111")) # Vergi Numarası veya TC Kimlik Numarası

>> True | False
```

### <img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/iterm2.svg"> CLI

```bash
eFatura 11111111111

# » [~] 11111111111 Numarası E-Fatura Mükellefi Değildir..
```

### <img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/freedesktop.svg"> UI

```bash
eFaturaGUI
```

## 📝 Proje Sahibi

- ✅ **[kmprens/CheckEinvoice](https://github.com/kmprens/CheckEinvoice)**

---

<details>
    <summary style="font-weight: bold; font-size: 20px">
      <img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/buddy.svg"> <b>Manuel Derlemek</b>
      <i>(genişletmek için tıklayın!)</i>
    </summary>
    <br/>

### <img width="16" src="https://raw.githubusercontent.com/keyiflerolsun/eFatura/main/.github/icons/python.svg"> Python

```bash
# Depoyu Çek
https://github.com/keyiflerolsun/eFatura.git
cd eFatura

# Gerekli Ortamları Kur
pip install -U pip setuptools wheel twine

# Paketi Yükle
pip install .

# Artıkları Temizle
rm -rf build *.egg-info

# Çalıştır
eFatura     # CLI
eFaturaGUI  # GUI

# Paketi Kaldır
pip uninstall eFatura
```
</details>

---

## 🌐 Telif Hakkı ve Lisans

* *Copyright (C) 2023 by* [keyiflerolsun](https://github.com/keyiflerolsun) ❤️️
* [GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007](https://github.com/keyiflerolsun/eFatura/blob/master/LICENSE) *Koşullarına göre lisanslanmıştır..*

## ♻️ İletişim

*Benimle iletişime geçmek isterseniz, **Telegram**'dan mesaj göndermekten çekinmeyin;* [@keyiflerolsun](https://t.me/KekikKahve)

## 💸 Bağış Yap

**[☕️ Kahve Ismarla](https://KekikAkademi.org/Kahve)**

***

> **[@KekikAkademi](https://t.me/KekikAkademi)** *için yazılmıştır..*
# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"

 
def test_sifre_gucu_detayli():
    
    assert sifre_gucu("12345678") == "orta"
    assert sifre_gucu("1234567") == "zayıf"

    
    assert sifre_gucu("123456789012") == "güçlü"
    assert sifre_gucu("12345678901") == "orta"

    
    assert sifre_gucu("cokuzunbirsiifre") == "güçlü"

def test_sifre_gucu_hata():
     
    with pytest.raises(ValueError):
        sifre_gucu("")


 
def test_otopark_ucreti_detayli():
   
    assert otopark_ucreti(15) == 0
    assert otopark_ucreti(16) == 20

   
    assert otopark_ucreti(60) == 20
    assert otopark_ucreti(61) == 40

    
    assert otopark_ucreti(180) == 40
    assert otopark_ucreti(181) == 60

    
    assert otopark_ucreti(0) == 0

def test_otopark_ucreti_hata():
     
    with pytest.raises(ValueError):
        otopark_ucreti(-1)


 
def test_yuzde_degisim_detayli():
    
    assert yuzde_degisim(200, 250) == 25.0
    assert yuzde_degisim(200, 150) == -25.0
    assert yuzde_degisim(100, 200) == 100.0  

def test_yuzde_degisim_hata():
    
    with pytest.raises(ValueError):
        yuzde_degisim(0, 50)
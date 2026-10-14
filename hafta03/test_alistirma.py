import pytest
from alistirma import kargo_ucreti, bilet_fiyati, ortalama

def test_kargo_buyuk_sipariste_ucretsiz():
    assert kargo_ucreti(600) == 0

@pytest.mark.parametrize("tutar, beklenen", [
    (500, 0),    # kargo-1 mutantını yakalar (tam sınır)
    (501, 0),
    (0, 50),     # kargo-2 mutantını yakalar (0 TL)
    (499, 50),
])
def test_kargo_ucreti(tutar, beklenen):
    assert kargo_ucreti(tutar) == beklenen

@pytest.mark.parametrize("tutar", [-1, -10])
def test_kargo_ucreti_hata(tutar):
    # kargo-3 mutantını yakalar (negatif tutar)
    with pytest.raises(ValueError):
        kargo_ucreti(tutar)

@pytest.mark.parametrize("yas, beklenen", [
    (0, 0),
    (6, 0),      # bilet-1 mutantını yakalar (6 yaş sınırı)
    (7, 50),     # bilet-2 mutantını yakalar (7 yaş / öğrenci sınırı)
    (17, 50),
    (18, 100),   # bilet-2 mutantını yakalar (18 yaş / tam bilet sınırı)
    (64, 100),
    (65, 60),    # bilet-3 mutantını yakalar (65 yaş sınırı)
])
def test_bilet_fiyati(yas, beklenen):
    assert bilet_fiyati(yas) == beklenen

@pytest.mark.parametrize("yas", [-1])
def test_bilet_fiyati_hata(yas):
    with pytest.raises(ValueError):
        bilet_fiyati(yas)

def test_ortalama_ondalikli():
    # ortalama-1 mutantını yakalar (ondalıklı / küsuratlı sonuç)
    assert ortalama([70, 85]) == 77.5

def test_ortalama_bos_liste():
    # ortalama-2 mutantını yakalar (boş liste hatası)
    with pytest.raises(ValueError):
        ortalama([])
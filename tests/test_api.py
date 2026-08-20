import pytest

def fungsi_validasi_kamera(id_kamera: str) -> bool:
    kamera_valid = ["CAM_LAB_01", "CAM_LAB_02"]
    return id_kamera in kamera_valid

def test_kamera_valid():
    assert fungsi_validasi_kamera("CAM_LAB_02") == True

def test_kamera_invalid():
    assert fungsi_validasi_kamera("CAM_MBG") == False
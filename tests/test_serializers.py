from asosiy.serializers import *
from unittest import TestCase

class Test_SuvSerializer(TestCase):
    def test_suv(self):
        suv = {
            "id": 1,
            "brend": "Family",
            "narx": 2000000,
            "litr": 200,
            "batafsil": "Buyurtmaga jo'natilyapti"
        }
        serializer = SuvSerializer(data=suv)
        assert serializer.is_valid() == True

class Test_MijozSerializer(TestCase):
    def test_mijoz(self):
        mijoz = {
            "id": 1,
            "ism": "Ali",
            "tel": "+998901232376",
            "manzil": "Farg'ona",
            "qarz": 1500000,
            "user": 1
        }
        serializer = MijozSerializer(data=mijoz)
        assert serializer.is_valid() == True

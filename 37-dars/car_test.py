import unittest
from cars import Car

class CarTest(unittest.TestCase):
    
    def setUp(self):
        make = "gm"
        self.model = "Malibu"
        year = 2020
        self.price = 40000
        self.km = 10000
        self.avto1 = Car(make,self.model,year)
        self.avto2 = Car(make,self.model,year,price=self.price)
        
    def test_create(self):
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshirish
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        # Qiymat mavjud emasligini assertIsNone metodi bilan tekshirish
        self.assertIsNone(self.avto1.price)
        # Qiymat tengligini assertEquals metodi bilan tekshirish
        self.assertEqual(0,self.avto1.get_km())
        
        # avto2 narhini tekshirish
        self.assertEqual(self.price,self.avto2.price)

    def test_set_price(self):
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price,self.avto2.price)
        
    def test_km(self):
        # Musbat qiymat berib tekshiramiz
        self.avto1.add_km(self.km)
        self.assertEqual(self.km,self.avto1.get_km())
        
        #Manfiy qiymat berib tekshiramiz
        new_km = -5000
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
            
unittest.main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
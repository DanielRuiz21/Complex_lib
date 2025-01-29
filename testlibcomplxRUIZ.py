import libcomplxRUIZ as lc
import unittest

class TestCplxOperations(unittest.TestCase):

    def testcplxsum(self):
        suma = lc.sumacomplx((2,5),(4,6))
        self.assertAlmostEqual(suma[0],6)
        self.assertAlmostEqual(suma[1],11)

        suma2 = lc.sumacomplx((3,6),(5,7))
        self.assertAlmostEqual(suma2[0],8)
        self.assertAlmostEqual(suma2[1],13)

    def testcplxrest(self):
        resta = lc.restcomplx((3,5),(-2.6,6.8))
        self.assertAlmostEqual(resta[0],5.6)
        self.assertAlmostEqual(resta[1],-1.8)

        resta2 = lc.restcomplx((8,4),(-2.6,6.8))
        self.assertAlmostEqual(resta2[0],10.6)
        self.assertAlmostEqual(resta2[1],-2.8)

    def testmultcplx(self):
        mult = lc.multcplx((2,6),(1,7))
        self.assertAlmostEqual(mult[0],-40)
        self.assertAlmostEqual(mult[1],20)

        mult2 = lc.multcplx((5,1),(2,8))
        self.assertAlmostEqual(mult2[0],2)
        self.assertAlmostEqual(mult2[1],42)

    def testconjugcomplx(self):
        self.assertEqual(lc.conjugcomplx((2,4)),(2,-4))

    def testdivcplx(self):
        div = lc.divcplx((4,1),(7,4))
        self.assertAlmostEqual(div[0],32/65)
        self.assertAlmostEqual(div[1],-9/65)
        div2 = lc.divcplx((8,4),(2,2))
        self.assertAlmostEqual(div2[0],3)
        self.assertAlmostEqual(div2[1],-1)

    def testmodulocomplx(self):
        modu = lc.modulocomplx((3,4))
        self.assertAlmostEqual(modu, 5)
        modu2 = lc.modulocomplx((6,8))
        self.assertAlmostEqual(modu2, 10)


    def testpolcar(self):
        self.assertEqual(lc.polcar((3,1.5)),(0.21,2.99))
        self.assertEqual(lc.polcar((4,0.8)),(2.79,2.87))

    def testcarpol(self):
        self.assertEqual(lc.carpol((3,4)),(5,0.93))
        self.assertEqual(lc.carpol((-2,5)),(5.39,-1.19))


    def testfase(self):
        self.assertAlmostEqual(lc.fasecomplx((4,-3)),-0.64)
        self.assertAlmostEqual(lc.fasecomplx((-2,5)),-1.19)




if __name__ == '__main__':
    unittest.main()

import unittest
from measurenary.similarity import *
import measurenary.utility as util


class TestSimilarity(unittest.TestCase):
    def setUp(self):
        # set up for a, b, c, d, n is positive, negative, and float
        self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n = 120, 30, 30, 20, 200
        self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n = -120, -30, -30, -20, -200
        self.float_a, self.float_b, self.float_c, self.float_d, self.float_n = 120.3, 30.2, 30.5, 20.2, 201.2

    def tearDown(self):
        pass

    def test_jaccard(self):
        self.assertAlmostEqual(jaccard(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.6666666666667)
        with self.assertRaises(ValueError):
            jaccard(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            jaccard(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_dice_2(self):
        self.assertAlmostEqual(dice_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.4)
        with self.assertRaises(ValueError):
            dice_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dice_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_dice_1(self):
        self.assertAlmostEqual(dice_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
        with self.assertRaises(ValueError):
            dice_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dice_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_three_way_jaccard(self):
        self.assertAlmostEqual(three_way_jaccard(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.857142857)
        with self.assertRaises(ValueError):
            three_way_jaccard(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            three_way_jaccard(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_neili(self):
        self.assertAlmostEqual(neili(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
        with self.assertRaises(ValueError):
            neili(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            neili(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_sokal_sneath_1(self):
        self.assertAlmostEqual(sokal_sneath_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.5)
        with self.assertRaises(ValueError):
            sokal_sneath_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            sokal_sneath_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_sokal_michener(self):
        self.assertAlmostEqual(sokal_michener(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.7)
        with self.assertRaises(ValueError):
            sokal_michener(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            sokal_michener(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_sokal_sneath_2(self):
        self.assertAlmostEqual(sokal_sneath_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.823529412)
        with self.assertRaises(ValueError):
            sokal_sneath_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            sokal_sneath_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_rogers_tanimoto(self):
        self.assertAlmostEqual(rogers_tanimoto(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.538461538)
        with self.assertRaises(ValueError):
            rogers_tanimoto(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            rogers_tanimoto(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_faith(self):
        self.assertAlmostEqual(faith(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.65)
        with self.assertRaises(ValueError):
            faith(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            faith(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_gower_legendre(self):
        self.assertAlmostEqual(gower_legendre(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.823529412)
        with self.assertRaises(ValueError):
            gower_legendre(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            gower_legendre(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_intersection(self):
        self.assertAlmostEqual(intersection(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 120)
        with self.assertRaises(ValueError):
            intersection(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            intersection(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_inner_product(self):
        self.assertAlmostEqual(inner_product(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 140)
        with self.assertRaises(ValueError):
            inner_product(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            inner_product(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_russell_rao(self):
        self.assertAlmostEqual(russell_rao(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.6)
        with self.assertRaises(ValueError):
            russell_rao(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            russell_rao(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    
    def test_cosine(self):
        self.assertAlmostEqual(cosine(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
        with self.assertRaises(ValueError):
            cosine(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            cosine(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_gilbert_wells(self):
        self.assertAlmostEqual(gilbert_wells(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.093109404)
        with self.assertRaises(ValueError):
            gilbert_wells(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            gilbert_wells(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_ochiai_1(self):
        self.assertAlmostEqual(ochiai_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
        with self.assertRaises(ValueError):
            ochiai_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            ochiai_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_forbes_1(self):
        self.assertAlmostEqual(forbes_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 1.066666667)
        with self.assertRaises(ValueError):
            forbes_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            forbes_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_fossum(self):
        self.assertAlmostEqual(fossum(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 126.9355556)
        with self.assertRaises(ValueError):
            fossum(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            fossum(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_sorgenfrei(self):
        self.assertAlmostEqual(sorgenfrei(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.64)
        with self.assertRaises(ValueError):
            sorgenfrei(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            sorgenfrei(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_mountford(self):
        self.assertAlmostEqual(mountford(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.026666667)
        with self.assertRaises(ValueError):
            mountford(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            mountford(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_otsuka(self):
        self.assertAlmostEqual(otsuka(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
        with self.assertRaises(ValueError):
            otsuka(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            otsuka(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_mc_connaughey(self):
        self.assertAlmostEqual(mc_connaughey(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.6)
        with self.assertRaises(ValueError):
            mc_connaughey(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            mc_connaughey(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_tarwid(self):
        self.assertAlmostEqual(tarwid(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.032258065)
        with self.assertRaises(ValueError):
            tarwid(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            tarwid(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_kulczynski_2(self):
        self.assertAlmostEqual(kulczynski_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
        with self.assertRaises(ValueError):
            kulczynski_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            kulczynski_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_driver_kroeber(self):
        self.assertAlmostEqual(driver_kroeber(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
        with self.assertRaises(ValueError):
            driver_kroeber(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            driver_kroeber(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_johnson(self):
        self.assertAlmostEqual(johnson(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 1.6)
        with self.assertRaises(ValueError):
            johnson(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            johnson(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_dennis(self):
        self.assertAlmostEqual(dennis(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.707106781)
        with self.assertRaises(ValueError):
            dennis(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dennis(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    
    def test_simpson(self):
        self.assertAlmostEqual(simpson(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
        with self.assertRaises(ValueError):
            simpson(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            simpson(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_braun_banquet(self):
        self.assertAlmostEqual(braun_banquet(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
        with self.assertRaises(ValueError):
            braun_banquet(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            braun_banquet(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_fager_mcgowan(self):
        self.assertAlmostEqual(fager_mcgowan(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), -74.2)
        with self.assertRaises(ValueError):
            fager_mcgowan(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            fager_mcgowan(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_forbes_2(self):
        self.assertAlmostEqual(forbes_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.2)
        with self.assertRaises(ValueError):
            forbes_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            forbes_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_sokal_sneath_4(self):
        self.assertAlmostEqual(sokal_sneath_4(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.6)
        with self.assertRaises(ValueError):
            sokal_sneath_4(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            sokal_sneath_4(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_gower(self):
        self.assertAlmostEqual(gower(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.018666667)
        with self.assertRaises(ValueError):
            gower(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            gower(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_pearson_1(self):
        self.assertAlmostEqual(pearson_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 8)
        with self.assertRaises(ValueError):
            pearson_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            pearson_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_pearson_2(self):
        self.assertAlmostEqual(pearson_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.196116135)
        with self.assertRaises(ValueError):
            pearson_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            pearson_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_pearson_3(self):
        self.assertAlmostEqual(pearson_3(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.031606977)
        with self.assertRaises(ValueError):
            pearson_3(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            pearson_3(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_pearson_heron_1(self):
        self.assertAlmostEqual(pearson_heron_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.2)
        with self.assertRaises(ValueError):
            pearson_heron_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            pearson_heron_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_pearson_heron_2(self):
        self.assertAlmostEqual(pearson_heron_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.36872065)
        with self.assertRaises(ValueError):
            pearson_heron_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            pearson_heron_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_sokal_sneath_3(self):
        self.assertAlmostEqual(sokal_sneath_3(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 2.333333333)
        with self.assertRaises(ValueError):
            sokal_sneath_3(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            sokal_sneath_3(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_sokal_sneath_5(self):
        self.assertAlmostEqual(sokal_sneath_5(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.000301699)
        with self.assertRaises(ValueError):
            sokal_sneath_5(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            sokal_sneath_5(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_cole(self):
        self.assertAlmostEqual(cole(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), None)
        with self.assertRaises(ValueError):
            cole(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            cole(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_stiles(self):
        self.assertAlmostEqual(stiles(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.84316354)
        with self.assertRaises(ValueError):
            stiles(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            stiles(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_ochiai_2(self):
        self.assertAlmostEqual(ochiai_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.32)
        with self.assertRaises(ValueError):
            ochiai_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            ochiai_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_yuleq(self):
        self.assertAlmostEqual(yuleq(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.454545455)
        with self.assertRaises(ValueError):
            yuleq(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            yuleq(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_yulew(self):
        self.assertAlmostEqual(yulew(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.240408206)
        with self.assertRaises(ValueError):
            yulew(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            yulew(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_kulczynski_1(self):
        self.assertAlmostEqual(kulczynski_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 2)
        with self.assertRaises(ValueError):
            kulczynski_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            kulczynski_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_tanimoto(self):
        self.assertAlmostEqual(tanimoto(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.666666667)
        with self.assertRaises(ValueError):
            tanimoto(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            tanimoto(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_disperson(self):
        self.assertAlmostEqual(disperson(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.0375)
        with self.assertRaises(ValueError):
            disperson(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            disperson(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_hamann(self):
        self.assertAlmostEqual(hamann(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.4)
        with self.assertRaises(ValueError):
            hamann(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            hamann(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_michael(self):
        self.assertAlmostEqual(michael(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.25862069)
        with self.assertRaises(ValueError):
            michael(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            michael(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_goodman_kruskal(self):
        self.assertAlmostEqual(goodman_kruskal(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.0)
        with self.assertRaises(ValueError):
            goodman_kruskal(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            goodman_kruskal(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_anderberg(self):
        self.assertAlmostEqual(anderberg(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.0)
        with self.assertRaises(ValueError):
            anderberg(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            anderberg(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_baroni_urbani_buser_1(self):
        self.assertAlmostEqual(baroni_urbani_buser_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.73797959)
        with self.assertRaises(ValueError):
            baroni_urbani_buser_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            baroni_urbani_buser_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_baroni_urbani_buser_2(self):
        self.assertAlmostEqual(baroni_urbani_buser_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.475959179)
        with self.assertRaises(ValueError):
            baroni_urbani_buser_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            baroni_urbani_buser_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_peirce(self):
        self.assertAlmostEqual(peirce(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.75)
        with self.assertRaises(ValueError):
            peirce(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            peirce(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_eyraud(self):
        self.assertAlmostEqual(eyraud(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 1.066666667)
        with self.assertRaises(ValueError):
            eyraud(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            eyraud(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_tarantula(self):
        self.assertAlmostEqual(tarantula(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 1.333333333)
        with self.assertRaises(ValueError):
            tarantula(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            tarantula(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_ample(self):
        self.assertAlmostEqual(ample(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 1.333333333)
        with self.assertRaises(ValueError):
            ample(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            ample(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_derived_rusell_rao(self):
        self.assertAlmostEqual(derived_rusell_rao(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.904302247)
        with self.assertRaises(ValueError):
            derived_rusell_rao(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            derived_rusell_rao(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_derived_jaccard(self):
        self.assertAlmostEqual(derived_jaccard(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.922534055)
        with self.assertRaises(ValueError):
            derived_jaccard(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            derived_jaccard(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    def test_var_of_correlation(self):
        self.assertAlmostEqual(var_of_correlation(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.106415687)
        with self.assertRaises(ValueError):
            var_of_correlation(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            var_of_correlation(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)


    # def test_positive(self):
    #     self.assertAlmostEqual(jaccard(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.6666666666667)
    #     self.assertAlmostEqual(dice_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.4)
    #     self.assertAlmostEqual(dice_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
    #     self.assertAlmostEqual(three_way_jaccard(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.857142857)
    #     self.assertAlmostEqual(neili(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
    #     self.assertAlmostEqual(sokal_sneath_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.5)
    #     self.assertAlmostEqual(sokal_michener(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.7)
    #     self.assertAlmostEqual(sokal_sneath_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.823529412)
    #     self.assertAlmostEqual(rogers_tanimoto(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.538461538)
    #     self.assertAlmostEqual(faith(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.65)
    #     self.assertAlmostEqual(gower_legendre(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.823529412)
    #     self.assertAlmostEqual(intersection(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 120)
    #     self.assertAlmostEqual(inner_product(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 140)
    #     self.assertAlmostEqual(russell_rao(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.6)
    #     self.assertAlmostEqual(cosine(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
    #     self.assertAlmostEqual(gilbert_wells(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.093109404)
    #     self.assertAlmostEqual(ochiai_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
    #     self.assertAlmostEqual(forbes_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 1.066666667)
    #     self.assertAlmostEqual(fossum(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 126.9355556)
    #     self.assertAlmostEqual(sorgenfrei(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.64)
    #     self.assertAlmostEqual(mountford(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.026666667)
    #     self.assertAlmostEqual(otsuka(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
    #     self.assertAlmostEqual(mc_connaughey(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.6)
    #     self.assertAlmostEqual(tarwid(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.032258065)
    #     self.assertAlmostEqual(kulczynski_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
    #     self.assertAlmostEqual(driver_kroeber(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
    #     self.assertAlmostEqual(johnson(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 1.6)
    #     self.assertAlmostEqual(dennis(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.707106781)
    #     self.assertAlmostEqual(simpson(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
    #     self.assertAlmostEqual(braun_banquet(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
    #     self.assertAlmostEqual(fager_mcgowan(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), -74.2)
    #     self.assertAlmostEqual(forbes_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.2)
    #     self.assertAlmostEqual(sokal_sneath_4(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.6)
    #     self.assertAlmostEqual(gower(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.018666667)
    #     self.assertAlmostEqual(pearson_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 8)
    #     self.assertAlmostEqual(pearson_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.196116135)
    #     self.assertAlmostEqual(pearson_3(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.031606977)
    #     self.assertAlmostEqual(pearson_heron_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.2)
    #     self.assertAlmostEqual(pearson_heron_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.36872065)
    #     self.assertAlmostEqual(sokal_sneath_3(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 2.333333333)
    #     self.assertAlmostEqual(sokal_sneath_5(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.000301699)
    #     self.assertAlmostEqual(cole(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), None)
    #     self.assertAlmostEqual(stiles(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.84316354)
    #     self.assertAlmostEqual(ochiai_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.32)
    #     self.assertAlmostEqual(yuleq(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.454545455)
    #     self.assertAlmostEqual(yulew(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.240408206)
    #     self.assertAlmostEqual(kulczynski_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 2)
    #     self.assertAlmostEqual(tanimoto(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.666666667)
    #     self.assertAlmostEqual(disperson(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.0375)
    #     self.assertAlmostEqual(hamann(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.4)
    #     self.assertAlmostEqual(michael(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.25862069)
    #     self.assertAlmostEqual(goodman_kruskal(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.0)
    #     self.assertAlmostEqual(anderberg(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.0)
    #     self.assertAlmostEqual(baroni_urbani_buser_1(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.73797959)
    #     self.assertAlmostEqual(baroni_urbani_buser_2(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.475959179)
    #     self.assertAlmostEqual(peirce(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.75)
    #     self.assertAlmostEqual(eyraud(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 1.066666667)
    #     self.assertAlmostEqual(tarantula(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 1.333333333)
    #     self.assertAlmostEqual(ample(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 1.333333333)
    #     self.assertAlmostEqual(derived_rusell_rao(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.904302247)
    #     self.assertAlmostEqual(derived_jaccard(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.922534055)

    # def test_negative(self):
    #     with self.assertRaises(ValueError):
    #         jaccard(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         dice_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n) 
    #         dice_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n) 
    #         three_way_jaccard(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         neili(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         sokal_sneath_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n) 
    #         sokal_michener(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n) 
    #         sokal_sneath_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         rogers_tanimoto(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         faith(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         gower_legendre(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         intersection(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         inner_product(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         russell_rao(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         cosine(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         gilbert_wells(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         ochiai_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         forbes_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         fossum(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         sorgenfrei(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         mountford(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         otsuka(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         mc_connaughey(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         tarwid(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         kulczynski_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         driver_kroeber(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         johnson(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         dennis(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         simpson(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n) 
    #         braun_banquet(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         fager_mcgowan(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         forbes_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         sokal_sneath_4(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         gower(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         pearson_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         pearson_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         pearson_3(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         pearson_heron_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         pearson_heron_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         sokal_sneath_3(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         sokal_sneath_5(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         cole(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         stiles(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         ochiai_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         yuleq(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         yulew(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         kulczynski_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         tanimoto(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         disperson(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         hamann(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         michael(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         goodman_kruskal(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         anderberg(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         baroni_urbani_buser_1(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         baroni_urbani_buser_2(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         peirce(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         eyraud(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         tarantula(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         ample(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         derived_rusell_rao(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
    #         derived_jaccard(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)

    # def test_float(self):
    #     with self.assertWarns(RuntimeWarning, msg="value in confusion matrix is not integer"):
    #         jaccard(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         dice_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n) 
    #         dice_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n) 
    #         three_way_jaccard(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         neili(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         sokal_sneath_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n) 
    #         sokal_michener(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n) 
    #         sokal_sneath_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         rogers_tanimoto(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         faith(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         gower_legendre(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         intersection(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         inner_product(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         russell_rao(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         cosine(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         gilbert_wells(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         ochiai_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         forbes_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         fossum(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         sorgenfrei(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         mountford(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         otsuka(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         mc_connaughey(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         tarwid(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         kulczynski_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         driver_kroeber(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         johnson(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         dennis(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         simpson(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n) 
    #         braun_banquet(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         fager_mcgowan(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         forbes_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         sokal_sneath_4(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         gower(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         pearson_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         pearson_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         pearson_3(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         pearson_heron_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         pearson_heron_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         sokal_sneath_3(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         sokal_sneath_5(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         cole(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         stiles(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         ochiai_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         yuleq(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         yulew(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         kulczynski_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         tanimoto(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         disperson(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         hamann(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         michael(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         goodman_kruskal(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         anderberg(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         baroni_urbani_buser_1(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         baroni_urbani_buser_2(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         peirce(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         eyraud(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         tarantula(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         ample(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         derived_rusell_rao(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    #         derived_jaccard(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
            
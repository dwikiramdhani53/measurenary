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

    def test_gleason(self):
        self.assertAlmostEqual(gleason(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.8)
        with self.assertRaises(ValueError):
            gleason(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            gleason(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_van_der_maarel(self):
        self.assertAlmostEqual(van_der_maarel(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.6)
        with self.assertRaises(ValueError):
            van_der_maarel(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            van_der_maarel(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_consonni_and_todeschini_iv(self):
        self.assertAlmostEqual(consonni_and_todeschini_iv(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.922534055)
        with self.assertRaises(ValueError):
            consonni_and_todeschini_iv(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            consonni_and_todeschini_iv(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_consonni_and_todeschini_iii(self):
        self.assertAlmostEqual(consonni_and_todeschini_iii(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.904302247)
        with self.assertRaises(ValueError):
            consonni_and_todeschini_iii(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            consonni_and_todeschini_iii(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
    
    def test_austin_and_colwell(self):
        self.assertAlmostEqual(austin_and_colwell(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.857504696)
        with self.assertRaises(ValueError):
            austin_and_colwell(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            austin_and_colwell(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_consonni_and_todeschini_i(self):
        self.assertAlmostEqual(consonni_and_todeschini_i(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.933146401)
        with self.assertRaises(ValueError):
            consonni_and_todeschini_i(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            consonni_and_todeschini_i(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_phi(self):
        self.assertAlmostEqual(phi(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.2)
        with self.assertRaises(ValueError):
            phi(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            phi(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_cohen(self):
        self.assertAlmostEqual(cohen(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 24.49489743)
        with self.assertRaises(ValueError):
            cohen(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            cohen(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_maxwell_and_pilliner(self):
        self.assertAlmostEqual(maxwell_and_pilliner(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 24.49489743)
        with self.assertRaises(ValueError):
            maxwell_and_pilliner(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            maxwell_and_pilliner(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_consonni_and_todeschini_v(self):
        self.assertAlmostEqual(consonni_and_todeschini_v(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.106415687)
        with self.assertRaises(ValueError):
            consonni_and_todeschini_v(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            consonni_and_todeschini_v(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_scott(self):
        self.assertAlmostEqual(scott(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.2)
        with self.assertRaises(ValueError):
            scott(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            scott(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_tetrachoric(self):
        self.assertAlmostEqual(tetrachoric(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.730476511)
        with self.assertRaises(ValueError):
            tetrachoric(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            tetrachoric(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_odds_ratio(self):
        self.assertAlmostEqual(odds_ratio(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 2.666666667)
        with self.assertRaises(ValueError):
            odds_ratio(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            odds_ratio(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_rand(self):
        self.assertAlmostEqual(rand(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.623115578)
        with self.assertRaises(ValueError):
            rand(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            rand(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_ARI(self):
        self.assertAlmostEqual(ARI(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.101290323)
        with self.assertRaises(ValueError):
            ARI(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            ARI(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_loevingers_H(self):
        self.assertAlmostEqual(loevingers_H(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.999998333)
        with self.assertRaises(ValueError):
            loevingers_H(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            loevingers_H(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_rogot_and_goldberg(self):
        self.assertAlmostEqual(rogot_and_goldberg(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.6)
        with self.assertRaises(ValueError):
            rogot_and_goldberg(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            rogot_and_goldberg(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_hawkins_and_dotson(self):
        self.assertAlmostEqual(hawkins_and_dotson(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.458333333)
        with self.assertRaises(ValueError):
            hawkins_and_dotson(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            hawkins_and_dotson(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_harris_and_lahey(self):
        self.assertAlmostEqual(harris_and_lahey(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 38.05555556)
        with self.assertRaises(ValueError):
            harris_and_lahey(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            harris_and_lahey(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_consonni_and_todeschini_ii(self):
        self.assertAlmostEqual(consonni_and_todeschini_ii(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.224846782)
        with self.assertRaises(ValueError):
            consonni_and_todeschini_ii(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            consonni_and_todeschini_ii(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)
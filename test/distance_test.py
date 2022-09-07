import unittest
import measurenary.distance as dis

class TestDistance(unittest.TestCase):
    def setUp(self):
        # set up for a, b, c, d, n is positive, negative, and float
        self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n = 120, 30, 30, 20, 200
        self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n = -120, -30, -30, -20, -200
        self.float_a, self.float_b, self.float_c, self.float_d, self.float_n = 120.3, 30.2, 30.5, 20.2, 201.2

    def tearDown(self):
        pass

    def test_hamming(self):
        self.assertAlmostEqual(dis.hamming(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 60)
        with self.assertRaises(ValueError):
            dis.hamming(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.hamming(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_euclidean(self):
        self.assertAlmostEqual(dis.euclidean(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 7.745966692)
        with self.assertRaises(ValueError):
            dis.euclidean(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.euclidean(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_squared_euclidean(self):
        self.assertAlmostEqual(dis.squared_euclidean(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 60)
        with self.assertRaises(ValueError):
            dis.squared_euclidean(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.squared_euclidean(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_canberra(self):
        self.assertAlmostEqual(dis.canberra(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 15.32618865)
        with self.assertRaises(ValueError):
            dis.canberra(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.canberra(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_manhattan(self):
        self.assertAlmostEqual(dis.manhattan(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 60)
        with self.assertRaises(ValueError):
            dis.manhattan(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.manhattan(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_mean_manhattan(self):
        self.assertAlmostEqual(dis.mean_manhattan(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.3)
        with self.assertRaises(ValueError):
            dis.mean_manhattan(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.mean_manhattan(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_cityblock(self):
        self.assertAlmostEqual(dis.cityblock(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 60)
        with self.assertRaises(ValueError):
            dis.cityblock(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.cityblock(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_minkowski(self):
        self.assertAlmostEqual(dis.minkowski(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 60)
        with self.assertRaises(ValueError):
            dis.minkowski(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.minkowski(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_vari(self):
        self.assertAlmostEqual(dis.vari(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.075)
        with self.assertRaises(ValueError):
            dis.vari(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.vari(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_size_difference(self):
        self.assertAlmostEqual(dis.size_difference(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.09)
        with self.assertRaises(ValueError):
            dis.size_difference(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.size_difference(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_shape_difference(self):
        self.assertAlmostEqual(dis.shape_difference(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.21)
        with self.assertRaises(ValueError):
            dis.shape_difference(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.shape_difference(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_pattern_difference(self):
        self.assertAlmostEqual(dis.pattern_difference(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.09)
        with self.assertRaises(ValueError):
            dis.pattern_difference(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.pattern_difference(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_lance_williams(self):
        self.assertAlmostEqual(dis.lance_williams(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.2)
        with self.assertRaises(ValueError):
            dis.lance_williams(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.lance_williams(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_bray_curtis(self):
        self.assertAlmostEqual(dis.bray_curtis(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.2)
        with self.assertRaises(ValueError):
            dis.bray_curtis(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.bray_curtis(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_hellinger(self):
        self.assertAlmostEqual(dis.hellinger(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.894427191)
        with self.assertRaises(ValueError):
            dis.hellinger(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.hellinger(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_chord(self):
        self.assertAlmostEqual(dis.chord(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.632455532)
        with self.assertRaises(ValueError):
            dis.chord(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.chord(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

    def test_yuleq_distance(self):
        self.assertAlmostEqual(dis.yuleq(self.pos_a, self.pos_b, self.pos_c, self.pos_d, self.pos_n), 0.545454545)
        with self.assertRaises(ValueError):
            dis.yuleq(self.neg_a, self.neg_b, self.neg_c, self.neg_d, self.neg_n)
        with self.assertWarns(RuntimeWarning):
            dis.yuleq(self.float_a, self.float_b, self.float_c, self.float_d, self.float_n)

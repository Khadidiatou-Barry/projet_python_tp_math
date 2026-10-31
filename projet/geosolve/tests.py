import unittest
from main import (
    distance_points,
    milieu_segment,
    resoudre_second_degre,
    intersection_droites,
    est_proche_zero
)

class TestGeoSolve(unittest.TestCase):

    def test_distance(self):
        resultat = distance_points(0, 0, 3, 4)
        self.assertAlmostEqual(resultat, 5)

    def test_milieu(self):
        resultat = milieu_segment(0, 2, 4, 6)
        self.assertEqual(resultat, (2, 4))

    def test_equation_second_degre(self):
        resultat = resoudre_second_degre(1, -5, 6)
        self.assertIn("Deux solutions", resultat)

    def test_droites_secantes(self):
        resultat = intersection_droites(1, 1, 5, 1, -1, 1)
        self.assertIn("(3.0, 2.0)", resultat)

    def test_droites_confondues(self):
        resultat = intersection_droites(1, 1, 5, 2, 2, 10)
        self.assertEqual(resultat, "Les droites sont confondues.")

    def test_droites_paralleles(self):
        resultat = intersection_droites(1, 1, 5, 1, 1, 8)
        self.assertIn("parallèles", resultat)

    def test_tolerance_numerique(self):
        resultat = est_proche_zero(1e-11, 2)
        self.assertTrue(resultat)

    def test_droites_presque_paralleles(self):
        resultat = intersection_droites(
            1, 1, 2,
            1, 1.00000000001, 3
        )
        self.assertIn("presque parallèles", resultat)


if __name__ == "__main__":
    unittest.main()
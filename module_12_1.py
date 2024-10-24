import runner
import unittest

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        verification_test = runner.Runner('Tom')
        for i in range(10):
            verification_test.walk()
        self.assertEqual(verification_test.distance, 50)

    def test_run(self):
        verification_test = runner.Runner('Ivan')
        for i in range(10):
            verification_test.run()
        self.assertEqual(verification_test.distance, 100)

    def test_challenge(self):
        obj1 = runner.Runner('Kat')
        obj2 = runner.Runner('Anna')
        for i in range(10):
            obj1.walk()
            obj2.run()
        self.assertNotEqual(obj1.distance, obj2.distance)


if __name__ == '__main__':
    unittest.main()

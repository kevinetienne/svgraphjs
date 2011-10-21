import unittest
from parser import SVGParser

filename = 'test.svg'

class SvgTest(unittest.TestCase):
    def setUp(self):
        self.svg = SVGParser()
        self.svg_parsed = self.svg.parse(filename)

    def test_data_parsed(self):
        self.assertTrue('svg' in self.svg.element,
                'should return an svg element')

if __name__ == "__main__":
    unittest.main()

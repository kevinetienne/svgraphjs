import unittest
from parser import SVGParser

filename = 'test.svg'

class SVGParserTest(unittest.TestCase):
    def setUp(self):
        self.svg_parser = SVGParser()
        self.svg_parsed = self.svg_parser.parse(filename)

    def test_data_parsed(self):
        self.assertTrue('svg' in self.svg_parser.element,
                'should return an svg element')

    def test_normalize(self):
        uri = "http://example.com/tags"
        tag = "tag"
        namespaced_element = "{%s}%s" % (uri, tag)
        normalized_uri, normalized_tag = self.svg_parser._normalize(namespaced_element)

        self.assertEqual(normalized_uri, uri,
                'should be equal') and \
                        self.assertEqual(normalized_tag, tag)

if __name__ == "__main__":
    unittest.main()

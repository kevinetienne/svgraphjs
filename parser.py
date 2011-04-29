import xml.etree.ElementTree as xml

class Svg(object):
    """
    convert a svg file to raphaeljs format
    """
    def __init__(self):
        self.path = []

    def parse(self, filename):
        tree = xml.parse(filename)
        root = tree.getroot()
        for item in root.getiterator():
            tag = self.normalize(item.tag)
            if isinstance(tag, tuple):
                name = tag[1]
            else:
                name = tag
            self.convert(name, item.attrib)

    def convert(self, name, item):
        if name == 'path':
            self.path.append(item)

    def parseChildren(self, element):
        return element.getchildren()

    def normalize(self, name):
        if name[0] == "{":
            uri, tag = name[1:].split("}")
            return (uri, tag)
        else:
            return name

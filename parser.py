from collections import defaultdict
import xml.etree.ElementTree as xml

class Svg(object):
    """
    convert a svg file to raphaeljs format
    """
    def __init__(self):
        self.element = defaultdict(list)
        self.element_understood = defaultdict(list)

    def parse(self, filename):
        """
        accepts as argument a filename
        """
        tree = xml.parse(filename)
        root = tree.getroot()
        for item in root.getiterator():
            tag = self._normalize(item.tag)
            if isinstance(tag, tuple):
                name = tag[1]
            else:
                name = tag
            self.element[name].append(item.attrib)

    def _normalize(self, name):
        if name[0] == "{":
            uri, tag = name[1:].split("}")
            return (uri, tag)
        else:
            return name

    def to_raphael(self):
        """
        """
        pass

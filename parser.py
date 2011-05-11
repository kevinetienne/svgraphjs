import xml.etree.ElementTree as xml

class Svg(object):
    """
    convert a svg file to raphaeljs format
    """
    def __init__(self):
        self.element = []

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
        # get position
        # can be replaced by another list containing a ref?
        key = self.position_for_key(name)
        if not key:
            self.element.append({name: []})
            key = len(self.element)-1

        self.element[key].get(name).append(item)

    def position_for_key(self, name):
        """ looks for a key in a list of dict """
        key = [k for k,v in enumerate(self.element) if name in v.keys()]
        if key:
            return key[0]

    def normalize(self, name):
        if name[0] == "{":
            uri, tag = name[1:].split("}")
            return (uri, tag)
        else:
            return name

    def get_item_by_name(self, name):
        try:
            element = next(element for element in self.element 
               if name in element.keys())
        except StopIteration
            return
        return element

    def to_raphael(self):
        """
        """
        pass


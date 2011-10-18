from collections import defaultdict
import xml.etree.ElementTree as xml

SVG_TAG = (
        'id',
        'width',
        'height')

RECT_ATTRS = ('id', 'x', 'y', 'width', 'height')

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

    def _quote_element(self, element):
        if element.isdigit():
            return int(element)
        else:
            return "\"%s\"" % element

    def _create_js_element(self, var, val, init=""):
        expression = ""
        if init:
            expression = "%s " % init
        expression += "%s = %s;" % (var, val)
        return expression

    def create_rect(self, rect):
        rectangle = []
        result = []
        if set(RECT_ATTRS).issubset(rect.keys()):
            expression = self._create_js_element(rect.get('id'),
                    "paper.rect(%(x)s,%(y)s,%(width)s,%(height)s)" % rect)
            rectangle.append(expression)

            if 'style' in rect.keys():
                style = rect.get('style').split(';')
                for element in style:
                    prop, value = element.split(":")
                    result.append("%s:%s" % 
                            (self._quote_element(prop), self._quote_element(value)))
                if result:
                    rectangle.append("%s.attr({%s})"% (rect.get('id'), 
                        ",".join(result)))
        return rectangle

    def to_raphael(self):
        """
        transforms the svg to raphael
        """
        result = []
        for tag, item in self.element.iteritems():
            if tag == 'svg':
                svg_element = dict((k,v) for k,v in item[0].iteritems()
                        if k in SVG_TAG)
                for k, v in svg_element.iteritems():
                    result.append("var %s = %s;" % (k, v));
            elif tag == 'rect':
                for rect in self.element.get('rect'):
                    result.extend(self.create_rect(rect))

        return result



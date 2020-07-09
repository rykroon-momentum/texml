from lxml import etree
from types import FunctionType
from exceptions import TeXMLError

class TeXMLElement:
    _name = ''
    _attributes = {}
    _nouns = []
    
    def __init__(self, *args, **kwargs):
        #set all attributes to None
        self.__dict__ = dict.fromkeys(self._attributes)

        #The text content inside the tag
        self.text = args[0] if args else None

        for attr, option in kwargs.items():

            #raise error if invalid attribute
            if attr not in self._attributes:
                raise TeXMLError(
                    "attribute '{}' not allowed for element '{}'".format(
                        attr, 
                        self._name
                    )
                )
            
            #raise error if invalid option
            options = self._attributes.get(attr)
            if options:

                #if options is a list
                if type(options) == list:
                    if option not in options:
                        raise TeXMLError(
                            "option '{}' not allowed for attribute '{}'".format(
                                option,
                                attr
                            )
                        )

                #if options is a function
                elif type(options) == FunctionType:
                    if not options(option):
                        raise TeXMLError(
                            "option '{}' not allowed for attribute '{}'".format(
                                option,
                                attr
                            )
                        )

            setattr(self, attr, option)

        self.children = []

    def append(self, element):
        if not isinstance(element, TeXMLElement):
            raise TeXMLError("element must be of type '{}'".format(TeXMLElement.__name__))

        if element._name not in self._nouns:
            raise TeXMLError(
                "'{}' element cannot be nested in a '{}' element".format(
                    element._name,
                    self._name
                )
            )

        self.children.append(element)
        return self

    def __repr__(self):
        return '{}({})'.format(self.__class__.__name__, self.children)

    def __str__(self):
        e = self._to_element()
        return etree.tostring(e, pretty_print=True, encoding='unicode')

    def _to_element(self, parent=None):
        if parent is None:
            e = etree.Element(self._name, vars(self))
        else:
            e = etree.SubElement(parent, self._name, vars(self))

        if self.text:
            e.text = self.text

        for child in self.children:
            child._to_element(parent=e)

        return e

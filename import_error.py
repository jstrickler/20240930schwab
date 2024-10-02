try:
    import lxml.etree as et
    NO_LXML = False
except ImportError as err:
    import xml.etree.ElementTree as et
    NO_LXML = True
#    print("module lxml not found -- please install before using this script")

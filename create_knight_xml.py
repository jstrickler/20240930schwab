import lxml.etree as et

root = et.Element("knight")
with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        name, title, color, quest, comment = raw_line.rstrip().split(':')
        knight_tag = et.SubElement(root, "knight", title=title)
        et.SubElement(knight_tag, "name").text = name
        color_tag = et.SubElement(knight_tag, "color")
        color_tag.text = color
        et.SubElement(knight_tag, "quest").text = quest
        et.SubElement(knight_tag, "comment").text = comment


xml_doc = et.tostring(root, pretty_print=True, xml_declaration=True).decode()
print(xml_doc)

doc = et.ElementTree(root)
doc.write('knights.xml', xml_declaration=True)

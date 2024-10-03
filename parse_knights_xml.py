import lxml.etree as et

doc = et.parse('knights.xml')

root = doc.getroot()
print(root)
for knight_tag in root:
    title = knight_tag.get('title')
    name = knight_tag.findtext('name')
    quest = knight_tag.findtext('quest')
    print(title, name, quest)

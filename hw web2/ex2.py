import mlab
from river import River

mlab.connect()

rivers = River.objects(continent="Africa")
print(len(rivers))
for r in rivers:
    print(r.name, sep="\n")


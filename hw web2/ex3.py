import mlab
from river import River

mlab.connect()

rivers = River.objects(continent="S. America",length__lt=1000)
print(len(rivers))
for r in rivers:
    print(r.name, sep="\n")


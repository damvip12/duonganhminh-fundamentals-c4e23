import mlab
from movies import Movie
from resource import Resource
from river import River

# from faker import Faker

# faker = Faker("en_US")

# for _ in range(5): #_ thay cho i vi minh k odung den bien' do'
#     print(faker.name())

mlab.connect()

# m = Movie.objects().with_id("5bf8019afb6fc0561fff7dc3")
# print(m.title)
# m.delete()


# movies_list = Movie.objects()

# for m in movies_list:
#     print(m.title,m.image,m.year,sep="/n")



# m = Movie(title="Batman", year = 2005, image = "https://www.sideshowtoy.com/wp-content/uploads/2017/11/dc-comics-justice-league-batman-statue-prime1-studio-feature-903246-1.jpg")
# # m.save()

# r = Resource(name="Tuan",city = "Ha Nam", yob=1962,height="158",weight="44") #chay nhieu lan de update
# r.save()

# resource_list = Resource.objects()

# r = Resource.objects().with_id("5bf7ffe39552eb1e709c76ed") #lay 1

# if r is None :
#     print("Not Found")
# else :
#     print("Found")
#     r.delete()

# resource_list = Resource.objects().first() #lay phan tu dau` tien.first() #lay nhieu objects ko co' j theo sau
# r = resource_list[0]
# r.delete()

# print(len(resource_list))

# for r in resource_list:
#     print(r.name,r.city,r.height)

from random import randint

# for _ in range(100):
#     name = faker.name()
#     city = faker.state()
#     yob = randint(1953,2000)
#     height = randint(150,200)
#     weight = randint(40,150)
#     r = Resource(name=name,city=city,yob=yob,height=height,weight=weight)
#     r.save()

# records = Resource.objects(name="Joe Schmidt")  #exact match
# # print(len(records))   #tim so luong name trong db match voi name dang tim`
# for r in records:
#     print(r.city,r.weight,r.height,sep="\n")
#     print("*********************")

# # for r in records:
# #     if r.name == "Joe Schmidt":  #qua dai`

# records = Resource.objects(height=172)
# for r in records :
#     print(r.name,r.city,r.weight,sep="\n")
#     print("---------------")


# records = Resource.objects(name__icontains="paul")  #search cho ca? hoa va` thuong`
# print(len(records))

# records = Resource.objects(height__gt=170)  #gt : greater than
# print(len(records))
# records = Resource.objects(name__icontains="Emily", height__lt=160)
# print(len(records))

# records = Resource.objects()

# for r in records:
#     r.update(set__available=False)

# r = Resource.objects().with_id("5bf80d1d9552eb1a2ca09c60")
# r.update(set__available=True)

rivers = River.objects(continent="Africa")
print(len(rivers))
for r in rivers:
    print(r.name, sep="\n")


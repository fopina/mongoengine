from mongoengine import *
connect(host='file://mydb')

class TestDoc(Document):
    some_name = StringField()

print('%d entries' % TestDoc.objects.count())
if TestDoc.objects.count() > 0:
	x = TestDoc.objects.all()[-1]
	print('%s with id %s' % (x.some_name, x.id))
TestDoc.objects.create(some_name='123')


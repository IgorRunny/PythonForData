from peewee import *

db = SqliteDatabase('orders.db')


class BaseModel(Model):
	class Meta:
		database = db


class Couriers(BaseModel):
	CourierID = IntegerField(primary_key=True, null=False)
	Surname = CharField()
	Name = CharField()
	Patronymic = CharField()
	PassportID = IntegerField()
	DateOfBirth = DateField()
	DateOfEmployment = DateField()
	StartWorkDay = TimeField()
	EndWorkDay = TimeField()
	City = CharField()
	Street = CharField()
	House = CharField()
	Flat = IntegerField()
	phone = CharField()

	class Meta:
		db_table = 'Couriers'


class Transports(BaseModel):
	CarNum = CharField(primary_key=True, null=False)
	Brand = CharField()
	DateOfRegistration = CharField()
	Color = CharField()

	class Meta:
		db_table = 'Transports'


class Senders(BaseModel):
	SenderID = IntegerField(primary_key=True, null=False)
	Surname = CharField()
	Name = CharField()
	Patronymic = CharField()
	DateOfBirth = DateField()
	Index = CharField()
	City = CharField()
	Street = CharField()
	House = CharField()
	Flat = IntegerField()
	Phone = CharField()

	class Meta:
		db_table = 'Senders'


Senders.create_table()


class Recipients(BaseModel):
	RecipientID = IntegerField(primary_key=True, null=False)
	Surname = CharField()
	Name = CharField()
	Patronymic = CharField()
	DateOfBirth = DateField()
	Index = CharField()
	City = CharField()
	Street = CharField()
	House = CharField()
	Flat = IntegerField()
	Phone = CharField()

	class Meta:
		db_table = 'Recipients'


Recipients.create_table()


class Orders(BaseModel):
	__tablename__ = 'Orders'
	OrderID = IntegerField(primary_key=True, null=False)
	SenderID = ForeignKeyField(Senders, related_name='SenderID', null=False)
	RecipientID = ForeignKeyField(Recipients, related_name='RecipientID', null=False)
	DateOfOrder = DateField()
	DateOfDelivery = DateField()
	PriceOfDelivery = DoubleField()
	CourierID = ForeignKeyField(Couriers, related_name='CourierID', null=False)
	TransportID = ForeignKeyField(Transports, related_name='TransportID', null=False)

	class Meta:
		db_table = 'Orders'


Orders.create_table()

sender1 = Senders.create(
	SenderID=1,
	Surname='Ivanov',
	Name='Ivan',
	Patronymic='Ivanovich',
	DateOfBirth='1980-01-01',
	Index='123456',
	City='Moscow',
	Street='Tverskaya',
	House='1',
	Flat='1',
	Phone='+7(999)999-99-99'
)
sender1.save()

sender2 = Senders.create(
	SenderID=2,
	Surname='Sergeev',
	Name='Sergey',
	Patronymic='Sergeevich',
	DateOfBirth='2000-01-01',
	Index='123333',
	City='Moscow',
	Street='Myasnitskaya',
	House='1',
	Flat='1',
	Phone='+7(999)123-99-99'
)
sender2.save()

recipient1 = Recipients.create(
	RecipientID=1,
	Surname='Petrov',
	Name='Petr',
	Patronymic='Petrovich',
	DateOfBirth='1990-01-01',
	Index='654321',
	City='Saint Petersburg',
	Street='Nevsky',
	House='10',
	Flat='20',
	Phone='+7(999)888-88-88'
)
recipient1.save()

recipient2 = Recipients.create(
	RecipientID=2,
	Surname='Sidorov',
	Name='Sidr',
	Patronymic='Sidorovich',
	DateOfBirth='1995-01-01',
	Index='654322',
	City='Saint Petersburg',
	Street='Liteyny',
	House='15',
	Flat='25',
	Phone='+7(999)777-77-77'
)
recipient2.save()

order1 = Orders.create(
	OrderID=1,
	SenderID=1,
	RecipientID=1,
	DateOfOrder='2024-01-01',
	DateOfDelivery='2024-01-02',
	PriceOfDelivery='1000',
	CourierID=1,
	TransportID='A123AA'
)
order1.save()

order2 = Orders.create(
	OrderID=2,
	SenderID=2,
	RecipientID=2,
	DateOfOrder='2024-01-03',
	DateOfDelivery='2024-01-04',
	PriceOfDelivery='1500',
	CourierID=1,
	TransportID='A123AA'
)
order2.save()
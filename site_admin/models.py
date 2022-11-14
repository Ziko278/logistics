from django.db import models
import random
import string


# Create your models here.
class SiteSetupModel(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200, null=True, blank=True)
    motto = models.CharField(max_length=200)
    logo = models.FileField(upload_to='images/logo', null=True, blank=True)
    mobile = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)


class CountryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name.upper()


class LocationModel(models.Model):
    city = models.CharField(max_length=100)
    country = models.ForeignKey(CountryModel, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.city.upper() + ' ' + self.country.name.upper()

    def save(self, *args, **kwargs):
        self.keyword = self.city.upper() + ' ' + self.country.name.upper()
        super(LocationModel, self).save()


class LogisticModel(models.Model):
    TYPE = (('individual', 'INDIVIDUAL'), ('company', 'COMPANY'))
    ITEM_TYPE = (
        ('chemical', 'CHEMICAL'),
        ('perishable', 'PERISHABLE'),
        ('document', 'DOCUMENT'),
        ('others', 'OTHERS'),
    )
    MODE = (
        ('freight', 'FREIGHT'),
        ('ship', 'SHIP'),
        ('land', 'LAND'),
    )
    client_type = models.CharField(max_length=20, choices=TYPE)
    client_name = models.CharField(max_length=200)
    client_address = models.TextField()
    client_number = models.CharField(max_length=20)

    retriever_type = models.CharField(max_length=20, choices=TYPE)
    retriever_name = models.CharField(max_length=200)
    retriever_number = models.CharField(max_length=20)
    retriever_address = models.TextField()

    title = models.CharField(max_length=200)
    item_type = models.CharField(max_length=20, choices=ITEM_TYPE)
    weight = models.FloatField()
    worth = models.FloatField()
    mode = models.CharField(max_length=20, choices=MODE)
    destination = models.CharField(max_length=200)
    tracking_id = models.CharField(max_length=20, blank=True)
    tracking_pin = models.CharField(max_length=20, blank=True)
    retrieval_id = models.CharField(max_length=20, blank=True)

    collection_date = models.DateTimeField(auto_now_add=True, blank=True)
    departure_date = models.DateTimeField()
    expected_date = models.DateTimeField()
    arrival_date = models.DateTimeField(blank=True, null=True)
    retrieval_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title.upper()

    def save(self, *args, **kwargs):
        if not self.tracking_id:
            while 1:
                tracking_id = random.choices(string.ascii_uppercase)[0] + random.choices(string.ascii_uppercase)[0] + str(random.randint(100000, 999999))
                logistic = LogisticModel.objects.filter(tracking_id=tracking_id)
                if not logistic:
                    break
            self.tracking_id = tracking_id
        if not self.retrieval_id:
            while 1:
                retrieval_id = str(random.choices(string.ascii_uppercase)[0]) + str(random.choices(string.ascii_uppercase)[0]) + str(random.randint(100000, 999999))
                logistic = LogisticModel.objects.filter(retrieval_id=retrieval_id)
                if not logistic:
                    break
            self.retrieval_id = retrieval_id
        super(LogisticModel, self).save()


class ShipmentProgressModel(models.Model):
    shipment = models.ForeignKey(LogisticModel, on_delete=models.CASCADE, related_name='shipment')
    title = models.CharField(max_length=200)
    comment = models.TextField()
    STATUS = (
        ('pending', 'PENDING'),
        ('start', 'START'),
        ('progress', 'PROGRESS'),
        ('success', 'SUCCESS'),
        ('error', 'ERROR'),
    )
    status = models.CharField(max_length=20, choices=STATUS)
    date = models.DateTimeField(blank=True, auto_now_add=True, null=True)

    def __str__(self):
        return self.shipment.title.title()






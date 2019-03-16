from django.db import models
from datetime import datetime

# Create your models here.
class ProductInfo(models.Model):
    sl_no = models.IntegerField()
    id = models.CharField(max_length=20, primary_key=True)
    name_of_product = models.CharField(max_length=255)
    type_of_product = models.CharField(max_length=100)
    firmware_version = models.CharField(max_length=50)
    os_supported = models.CharField(max_length=100)
    supported_protocols = models.CharField(max_length=255)
    max_firmware_support = models.CharField(max_length=100)
    env_support = models.CharField(max_length=100)
    power_capability = models.CharField(max_length=50)
    pricing = models.BigIntegerField()
    configurable = models.IntegerField()
    desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return " %s %s %s %s %s %s %s %s %s %s %s %s %s" % (self.sl_no,
                                                            self.id,
                                                            self.name_of_product,
                                                            self.type_of_product,
                                                            self.firmware_version,
                                                            self.os_supported,
                                                            self.supported_protocols,
                                                            self.max_firmware_support,
                                                            self.env_support,
                                                            self.power_capability,
                                                            self.pricing,
                                                            self.configurable,
                                                            self.desc)


class ProductionProductInfo(models.Model):
    sl_no = models.IntegerField()
    name_of_product = models.CharField(max_length=100)
    type_of_product = models.CharField(max_length=100)
    firmware_version = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    customer_id = models.CharField(max_length=50)
    last_Upgraded = models.DateTimeField(default=datetime.now, blank=True)
    validity = models.DateTimeField(default=datetime.now, blank=True)
    alarms = models.TextField()
    health = models.IntegerField()
    auto_recovery = models.IntegerField()
    last_rebooted = models.DateTimeField(default=datetime.now, blank=True)
    system_crash_report = models.TextField()
    security = models.CharField(max_length=150)
    authority = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s" %(self.sl_no,
                                                                self.name_of_product,
                                                                self.type_of_product,
                                                                self.firmware_version,
                                                                self.username,
                                                                self.customer_id,
                                                                self.last_Upgraded,
                                                                self.validity,
                                                                self.alarms,
                                                                self.health,
                                                                self.auto_recovery,
                                                                self.last_rebooted,
                                                                self.system_crash_report,
                                                                self.security,
                                                                self.authority)


star_rating = (
    ('1','*'),
    ('2', '**'),
    ('3', '***'),
    ('4', '****'),
    ('5', '*****')
)

class ProductFeedback(models.Model):
    username = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    services = models.TextField()
    product_quality = models.CharField(choices=star_rating, max_length=10)
    suggestions = models.TextField()
    future_scope = models.TextField()

    def __str__(self):
        return "%s %s %s %s %s %s %s " % (self.username,
                                          self.product_name,
                                          self.product_type,
                                          self.services,
                                          self.product_quality,
                                          self.suggestions,
                                          self.future_scope)
from __future__ import unicode_literals

from django.db import models
from datetime import datetime, time   
from time import timezone
from django.utils import timezone
from django.views.generic import ListView
# Create your models here.
class BEER_DIM(models.Model):
    BEER_ID = models.CharField(db_column='BEER_ID', primary_key=True, max_length=6)  # Field name made lowercase.
    CATEGORY_ID = models.IntegerField(db_column='CATEGORY_ID', blank=True, null=True)  # Field name made lowercase.
    STYLE_ID = models.IntegerField(db_column='STYLE_ID', blank=True, null=True)  # Field name made lowercase.
    GLASS_ID = models.IntegerField(db_column='GLASS_ID', blank=True, null=True)  # Field name made lowercase.
    NAME = models.CharField(db_column='NAME', max_length=100)  # Field name made lowercase.
    NAME_DISPLAY = models.CharField(db_column='NAME_DISPLAY', max_length=100, blank=True, null=True)  # Field name made lowercase.
    DESCRIPTION = models.CharField(max_length=2000, blank=True, null=True)
    ABV = models.DecimalField(db_column='ABV', max_digits=5, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    IBU = models.DecimalField(db_column='IBU', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    SRM_ID = models.IntegerField(db_column='SRM_ID', blank=True, null=True)  # Field name made lowercase.
    AVAILABLE_ID = models.IntegerField(db_column='AVAILABLE_ID', blank=True, null=True)  # Field name made lowercase.
    IS_ORGANIC = models.CharField(db_column='IS_ORAGNIC', max_length=1, blank=True, null=True)  # Field name made lowercase.
    STATUS = models.CharField(db_column='STATUS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    STATUS_DISPLAY = models.CharField(db_column='STATUS_DISPLAY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    SERVING_TEMP = models.CharField(db_column='SERVING_TEMP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    SERVING_TEMP_DISPLAY = models.CharField(db_column='SERVING_TEMP_DISPLAY', max_length=50, blank=True, null=True)  # Field name made lowercase.
    LABEL_SMALL = models.CharField(db_column='LABEL_SMALL', max_length=100, blank=True, null=True)  # Field name made lowercase.
    LABEL_MEDIUM = models.CharField(db_column='LABEL_MEDIUM', max_length=100, blank=True, null=True)  # Field name made lowercase.
    LABEL_LARGE = models.CharField(db_column='LABEL_LARGE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    CREATE_DATE = models.DateTimeField(null=True)
    UPDATE_DATE = models.DateTimeField(null=True)
        
    class Meta:
        app_label = 'drinkinfo'
    def __unicode__(self):
        return "%s" % (self.NAME)


        
        
class SPECIALS_HDR_FCT(models.Model):
    TIME_CHOICES = (
    (time(00, 00, 00), u'12 AM'), 
    (time(01, 00, 00), u'1 AM'), 
    (time(01, 00, 00), u'1 AM'), 
    (time(03, 00, 00), u'3 AM'), 
    (time(04, 00, 00), u'4 AM'), 
    (time(05, 00, 00), u'5 AM'), 
    (time(06, 00, 00), u'6 AM'), 
    (time(07, 00, 00), u'7 AM'),
    (time(8, 00, 00), u'8 AM'), 
    (time(9, 00, 00), u'9 AM'), 
    (time(10, 00, 00), u'10 AM'), 
    (time(11, 00, 00), u'11 AM'), 
    (time(12, 00, 00), u'12 PM'), 
    (time(13, 00, 00), u'1 PM'), 
    (time(14, 00, 00), u'2 PM'), 
    (time(15, 00, 00), u'3 PM'), 
    (time(16, 00, 00), u'4 PM'), 
    (time(17, 00, 00), u'5 PM'), 
    (time(18, 00, 00), u'6 PM'), 
    (time(19, 00, 00), u'7 PM'), 
    (time(20, 00, 00), u'8 PM'), 
    (time(21, 00, 00), u'9 PM'), 
    (time(22, 00, 00), u'10 PM'), 
    (time(23, 00, 00), u'11 PM'),
)

    SPECIAL_HDR_ID = models.AutoField(primary_key=True)
    SPECIAL_HDR_DESC = models.CharField(max_length=100, blank=True, null=True)  # Field name made lowercase.
    LOCATION_KEY = models.ForeignKey('LOCATION_DIM', default=-1)
    START_TIME = models.TimeField(null=False, choices=TIME_CHOICES,default = time(00, 00, 00))  # Field name made lowercase.
    END_TIME = models.TimeField(null=False, choices=TIME_CHOICES, default = time(23, 00, 00))    # Field name made lowercase.
    DAY_MON_FLG = models.BooleanField(default=False)
    DAY_TUE_FLG = models.BooleanField(default=False)
    DAY_WED_FLG = models.BooleanField(default=False)
    DAY_THU_FLG = models.BooleanField(default=False)
    DAY_FRI_FLG = models.BooleanField(default=False)
    DAY_SAT_FLG = models.BooleanField(default=False)
    DAY_SUN_FLG = models.BooleanField(default=False)
    CREATE_DATE = models.DateTimeField(default=timezone.now)
    UPDATE_DATE = models.DateTimeField(default=timezone.now)

     
    class Meta:
        app_label = 'drinkinfo'
    

class SPECIALS_LN_FCT(models.Model):
    SPECIAL_LN_ID = models.AutoField(primary_key=True)
    SPECIAL_HDR_ID = models.ForeignKey('SPECIALS_HDR_FCT',on_delete=models.CASCADE ,default=-1)
    BEER_ID = models.ForeignKey('BEER_DIM', default=-1)
    SERVING_SIZE = models.IntegerField(default=0)
    PRICE_AMT = models.DecimalField(max_digits=8, decimal_places=2,default = 0)
    CREATE_DATE = models.DateTimeField(default=timezone.now)
    UPDATE_DATE = models.DateTimeField(default=timezone.now)
    class Meta:
        app_label = 'drinkinfo'
 
    
class LOCATION_DIM(models.Model):
    LOCATION_KEY = models.AutoField(default=1,primary_key=True)
    PLACE_ID = models.CharField(max_length=100, null=False)
    PLACE_NAME = models.CharField(max_length=50, null=False)
    class Meta:
        app_label = 'drinkinfo'
    def __unicode__(self):
        return "%s" % (self.PLACE_NAME)



class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



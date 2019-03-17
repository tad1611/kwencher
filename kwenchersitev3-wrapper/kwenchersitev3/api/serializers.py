from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')
#         
# class BeerSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = BEER_DIM
#         fields = ('beer_id','category_id','style_id','glass_id','name','name_display','description','abv','ibu','srm_id','available_id','is_oragnic','status','status_display','serving_temp','serving_temp_display','label_small','label_medium','label_large','create_date','update_date')
# 
# class SpecialsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = SPECIALS_FCT
#         fields = (
# 'special_id',
# 'name',
# 'beer_glass_name',
# 'beer_glass_size',
# 'location_lng',
# 'location_lat',
# 'price_amt',
# 'start_time',
# 'end_time',
# 'day_mon_flg',
# 'day_tue_flg',
# 'day_wed_flg',
# 'day_thur_flg',
# 'day_fri_flg',
# 'day_sat_flg',
# 'day_sun_flg');
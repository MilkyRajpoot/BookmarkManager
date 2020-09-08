from rest_framework import serializers
from . models import *

class customerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'  
        # fields = ('id', 'location') 

class bookmarkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark
        fields = '__all__' 
        # fields = ('id', 'title', 'url', 'source_name')   

class browsecusbookSerializer(serializers.ModelSerializer):
	customer = customerSerializer(read_only=True)
	bookmark = bookmarkSerializer(read_only=True)

	class Meta:
		model = CustomerBookmark
		fields = ('id', 'bookmark', 'customer', 'created_at', 'updated_at') 

class cusbookSerializer(serializers.ModelSerializer):

	class Meta:
		model = CustomerBookmark
		fields = ('id', 'created_at', 'updated_at') 

from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.urls import reverse_lazy

# we made accounts app to handel the user instad of is number in jaon format
User=get_user_model()

class UserDisplaySerializer(serializers.ModelSerializer):
	Follower_count=serializers.SerializerMethodField()
	url=serializers.SerializerMethodField()

	class Meta:
		model=User
		fields=[
		    'username',
		    'first_name',
		    'last_name',
		    'Follower_count',
		    'url',

		    #'email'
		]

	def get_Follower_count(self,obj) :
		return 0

	 
	def get_url(self,obj):
		return reverse_lazy("profiles:detail",kwargs={"username":obj.username})

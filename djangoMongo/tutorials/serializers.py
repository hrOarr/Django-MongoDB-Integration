from rest_framework import serializers 
from tutorials.models import Tutorial
 
 
class TutorialSerializer(serializers.ModelSerializer):

    author_full_name = serializers.CharField()

    class Meta:
        model = Tutorial
        fields = ['id',
                  'title',
                  'author_full_name',
                  'slug',
                  'content',
                  'img1',
                  'created_on']
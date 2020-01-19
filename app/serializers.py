from app.models import Post, Category  
from rest_framework import serializers  


class PostSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Post  
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(many=True)
    class Meta:
        model = Category
        fields = '__all__'
        
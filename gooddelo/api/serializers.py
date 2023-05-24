from rest_framework import serializers
from tasks.models import User, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'created_at', 'updated_at', 'author')
        read_only_fields = ('created_at', 'updated_at', 'author')

    def create(self, validated_data):
        task = Task.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            author=self.context['request'].user
        )
        return task

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

from rest_framework import serializers

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, allow_null=False, max_length=120)
    content = serializers.CharField(required=True, max_length=3000, allow_null=False)
    author = serializers.PrimaryKeyRelatedField(read_only=True)

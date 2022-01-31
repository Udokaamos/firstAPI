from rest_framework import serializers
from main.models import Song

class SongSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(max_length = 255, write_only=True)

    class Meta:
        model = Song
        # fields = '__all__'
        fields = ['title', 'artist', 'publish_date', 'date_created']
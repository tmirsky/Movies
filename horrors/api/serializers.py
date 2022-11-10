from rest_framework.serializers import ModelSerializer
from slugify import slugify

from horrors.movies.models import Reviews


class ReviewSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data.update({'slug': slugify(validated_data.get('title') + validated_data.get('subtitle')) + ' ' + str(validated_data.get('id'))})
        review = Reviews(**validated_data)
        review.save()
        return review

    class Meta:
        model = Reviews
        fields = ('id', 'name', 'text', 'movie')

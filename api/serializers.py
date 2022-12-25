from django.utils.text import slugify
from rest_framework import serializers

from myshop.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ('slug', 'created', 'updated')

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data.get('name'))
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        super(ProductSerializer, self).update(instance, validated_data)
        instance.slug = slugify(validated_data.get('name', instance.slug))
        instance.save()
        return instance


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ('slug',)

    def create(self, validated_data):
        validated_data['slug'] = slugify(validated_data.get('slug'))
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        super(CategorySerializer, self).update(instance, validated_data)
        instance.slug = slugify(validated_data.get('name', instance.slug))
        instance.save()
        return instance

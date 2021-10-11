from rest_framework import serializers

from books.models import Book, Author, Publisher, Country


class BookAPISerializer(serializers.Serializer):
    """
    Serializer for Ice and Fire API to retrieve books.
    """
    name = serializers.CharField()
    isbn = serializers.CharField()
    authors = serializers.ListField()
    publisher = serializers.CharField()
    number_of_pages = serializers.IntegerField(source="numberOfPages")
    country = serializers.CharField()
    release_date = serializers.DateField(source="released", format="%d-%m-%Y")


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializer for Author model.
    """
    class Meta:
        model = Author
        fields = ('name',)

    def to_representation(self, instance):
        """
        external representation of serialized data for Author model.
        """
        return instance.name

    def to_internal_value(self, data):
        """
        internal value of serialized data for Author model.
        """
        try:
            return Author.objects.get(name=data)
        except Author.DoesNotExist:
            raise serializers.ValidationError("{} Author does not exist.".format(data))


class CountrySerializer(serializers.ModelSerializer):
    """
    Serializer for Country model.
    """
    class Meta:
        model = Country
        fields = ('name', )

    def to_representation(self, instance):
        """
        external representation of serialized data for Country model.
        """
        return instance.name

    def to_internal_value(self, data):
        """
        internal value of serialized data for Country model.
        """
        try:
            return Country.objects.get(name=data)
        except Country.DoesNotExist:
            raise serializers.ValidationError("{} Country does not exist.".format(data))


class PublisherSerializer(serializers.ModelSerializer):
    """
    Serializer for Publisher model.
    """
    class Meta:
        model = Publisher
        fields = ('name', )

    def to_representation(self, instance):
        """
        external representation of serialized data for Publisher model.
        """
        return instance.name

    def to_internal_value(self, data):
        """
        internal value of serialized data for Publisher model.
        """
        try:
            return Publisher.objects.get(name=data)
        except Publisher.DoesNotExist:
            raise serializers.ValidationError("{} Publisher does not exist.".format(data))


class BookModelSerializer(serializers.ModelSerializer):
    """
    Serializer for Book model.
    """
    release_date = serializers.DateTimeField(source="released_date", format="%Y-%m-%d")
    authors = AuthorSerializer(many=True)
    publisher = PublisherSerializer()
    country = CountrySerializer()

    class Meta:
        model = Book
        fields = ('id', 'name', 'isbn', 'authors', 'number_of_pages', 'publisher', 'country', 'release_date')

    def create(self, validated_data):
        """
        Creation of new Book after serializer validated.
        """
        authors = validated_data.pop('authors')
        new_book = Book.objects.create(**validated_data)
        new_book.authors.add(*authors)
        new_book.save()
        return new_book

    def update(self, instance, validated_data):
        """
        Update specified Book instance with validated data
        """
        instance.name = validated_data.get('name', instance.name)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.country = validated_data.get('country', instance.country)
        if validated_data.get('author'):
            instance.authors.add(*validated_data.get('authors'))
        instance.released_date = validated_data.get('released_date', instance.released_date)
        instance.number_of_pages = validated_data.get('number_of_pages', instance.number_of_pages)
        instance.publisher = validated_data.get('publisher', instance.publisher)
        instance.save()
        return instance

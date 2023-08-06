from django.db import models
from ckeditor.fields import RichTextField  # Import RichTextField from ckeditor.fields

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Listing(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content_arabic = RichTextField()  # Use RichTextField instead of TextField
    translation = models.TextField()
    description = models.TextField()
    published = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Like(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    total_likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.listing.title} - {self.total_likes} likes"

class Report(models.Model):
    LIST_TYPES = (
        ('harmful', 'Harmful'),
        ('false', 'False'),
        # Add more types as needed
    )
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    list_type = models.CharField(choices=LIST_TYPES, max_length=20)

    def __str__(self):
        return f"{self.listing.title} - {self.get_list_type_display()} Report"

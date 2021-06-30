from django.db import models


class CategoryModel(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class NewsModel(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(upload_to='media')
    category = models.ForeignKey(CategoryModel, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

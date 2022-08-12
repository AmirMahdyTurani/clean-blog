from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=255, db_index=True, verbose_name="عنوان مقاله")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts", default=1, db_index=True,
                               verbose_name="نویسنده")
    short_description = models.CharField(max_length=355, null=True, verbose_name="توضیحات کوتاه")
    slug = models.SlugField(unique=True, db_index=True, verbose_name="لینک")
    photo = models.ImageField(upload_to='images')
    published = models.DateField(db_index=True, verbose_name="تاریخ انتشار")
    description = RichTextField(verbose_name="متن مقاله")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

    def __str__(self):
        return f"{self.title} | {self.author}"

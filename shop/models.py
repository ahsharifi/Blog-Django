from django.db import models

class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="نام دسته بندی",
    )

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200, verbose_name="نام محصول")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="لینک")
    description = models.TextField(null=True, blank=True, verbose_name="توضیحات")
    price = models.DecimalField(max_digits=12, decimal_places=0, verbose_name="قیمت")
    category_id = models.ForeignKey(Category, models.CASCADE, null=True, verbose_name="دسته بندی")
    status = models.BooleanField(verbose_name="وضعیت", default=True)

    def __str__(self):
        return self.title

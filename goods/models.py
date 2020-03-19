
from djmoney.models.fields import MoneyField
from django.utils.safestring import mark_safe
from django.conf import settings
from django.db import models
from django.utils import timezone


class Goods(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, help_text='автор', blank=True)
    slug = models.SlugField(max_length=128, blank=True)
    title = models.CharField(verbose_name='название', max_length=200, blank=True)
    description = models.TextField(verbose_name='описание')

    pln_price = MoneyField(verbose_name='злотые', help_text='цена в злотых', max_digits=14, decimal_places=2, default_currency='PLN')
    uah_price = MoneyField(verbose_name='гривна', help_text='цена в гривне', max_digits=14, decimal_places=2, default_currency='UAH')
    sale_price = MoneyField(verbose_name='цена', help_text='цена продажи', max_digits=14, decimal_places=2, default_currency='UAH')
    sales = models.BooleanField(verbose_name='продано', help_text='статус', default=False)
    height = models.PositiveIntegerField(default=150, blank=True)
    width = models.PositiveIntegerField(default=150, blank=True)
    image = models.ImageField(verbose_name='изображение', upload_to="goods_image", blank=True, null=True, height_field='height', width_field='width')    
    created_date = models.DateTimeField(verbose_name='добавлено', default=timezone.now)

    class Meta:
        verbose_name_plural = "Товары"
        verbose_name = "Одежда"

    def __str__(self):
        return self.title

    def get_image(self):
        if not self.image:
            return 1
        return self.image.url
 
    # method to create a fake table field in read only mode
    def image_tag(self):
        return mark_safe('<img src="%s" width="100" height="100" />' % self.get_image())
 
    image_tag.short_description = 'Image'

# Generated by Django 2.2.11 on 2020-03-12 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='height',
            field=models.PositiveIntegerField(blank=True, default=150),
        ),
        migrations.AddField(
            model_name='goods',
            name='width',
            field=models.PositiveIntegerField(blank=True, default=150),
        ),
        migrations.AlterField(
            model_name='goods',
            name='author',
            field=models.ForeignKey(help_text='автор', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='goods',
            name='image',
            field=models.ImageField(blank=True, height_field='height', null=True, upload_to='goods_image', verbose_name='изображение', width_field='width'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='pln_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('UAH', 'Hryvnia'), ('PLN', 'Zloty')], default='PLN', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='goods',
            name='sale_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('UAH', 'Hryvnia'), ('PLN', 'Zloty')], default='UAH', editable=False, max_length=3),
        ),
        migrations.AlterField(
            model_name='goods',
            name='sales',
            field=models.BooleanField(default=False, help_text='статус', verbose_name='продано'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='uah_price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('UAH', 'Hryvnia'), ('PLN', 'Zloty')], default='UAH', editable=False, max_length=3),
        ),
    ]

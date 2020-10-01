# Generated by Django 3.0.7 on 2020-09-07 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200907_0639'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('s', 'Shirt'), ('sw', 'SportWear'), ('ow', 'Outwear')], default='S', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('S', 'secondary'), ('P', 'primary'), ('D', 'danger')], default='test description', max_length=2),
            preserve_default=False,
        ),
    ]
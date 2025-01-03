# Generated by Django 5.1.4 on 2025-01-02 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_productitem_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='productcategory',
            name='category_image',
            field=models.ImageField(default=0, upload_to='category_images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='productcategory',
            name='slug',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
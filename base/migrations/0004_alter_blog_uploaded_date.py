# Generated by Django 3.2.12 on 2022-12-07 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_alter_blog_uploaded_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='uploaded_date',
            field=models.DateField(),
        ),
    ]
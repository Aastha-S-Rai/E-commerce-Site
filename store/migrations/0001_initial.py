# Generated by Django 3.2.14 on 2022-10-03 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(default='', max_length=50)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='uploads/products/')),
            ],
        ),
    ]
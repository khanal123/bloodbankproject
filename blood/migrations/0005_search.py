# Generated by Django 3.2 on 2023-05-12 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0004_bloodrequest_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]
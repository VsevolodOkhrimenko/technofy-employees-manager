# Generated by Django 2.1.1 on 2019-02-26 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sector',
            name='standardized',
            field=models.BooleanField(default=False),
        ),
    ]
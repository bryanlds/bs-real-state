# Generated by Django 3.0 on 2019-12-24 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("listings", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="listing",
            name="photo_main",
            field=models.ImageField(default=None, upload_to="photos/%Y/%m/%d/"),
            preserve_default=False,
        )
    ]

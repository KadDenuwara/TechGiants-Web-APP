# Generated by Django 4.2.2 on 2024-06-24 17:34

from django.db import migrations
import django_ckeditor_5.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_review_delete_productreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='description_long',
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]
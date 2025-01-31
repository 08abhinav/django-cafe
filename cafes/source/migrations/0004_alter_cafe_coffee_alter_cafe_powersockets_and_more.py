# Generated by Django 5.1.1 on 2024-09-26 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('source', '0003_alter_cafe_coffee_alter_cafe_wifi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='coffee',
            field=models.CharField(choices=[('☆', '☆'), ('☆☆', '☆☆'), ('☆☆☆', '☆☆☆'), ('☆☆☆☆', '☆☆☆☆'), ('☆☆☆☆☆', '☆☆☆☆☆')], default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='powersockets',
            field=models.CharField(choices=[('☆', '☆'), ('☆☆', '☆☆'), ('☆☆☆', '☆☆☆'), ('☆☆☆☆', '☆☆☆☆'), ('☆☆☆☆☆', '☆☆☆☆☆')], default=0, max_length=5),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='wifi',
            field=models.CharField(choices=[('☆', '☆'), ('☆☆', '☆☆'), ('☆☆☆', '☆☆☆'), ('☆☆☆☆', '☆☆☆☆'), ('☆☆☆☆☆', '☆☆☆☆☆')], default=0, max_length=5),
        ),
    ]

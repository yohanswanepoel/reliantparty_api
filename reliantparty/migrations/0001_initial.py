# Generated by Django 2.0.3 on 2019-09-06 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReliantParty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('status', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('abn', models.CharField(max_length=255)),
            ],
        ),
    ]
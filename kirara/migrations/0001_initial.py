# Generated by Django 2.1.7 on 2019-02-16 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('hp', models.IntegerField()),
                ('atk', models.IntegerField()),
                ('matk', models.IntegerField()),
                ('dif', models.IntegerField()),
                ('mdif', models.IntegerField()),
                ('spd', models.IntegerField()),
                ('rare', models.IntegerField(choices=[(3, 3), (4, 4), (5, 5)], default=5)),
                ('skill', models.IntegerField()),
            ],
        ),
    ]
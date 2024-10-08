# Generated by Django 3.2.25 on 2024-07-09 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(max_length=50)),
                ('ingredient_price', models.FloatField()),
                ('ingredient_type', models.IntegerField(choices=[(0, 'fish'), (1, 'meat'), (2, 'vegetables')], default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Povar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Povar_name', models.CharField(max_length=50)),
                ('Povar_experience', models.IntegerField()),
                ('Povar_rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=50)),
                ('dish_price', models.FloatField()),
                ('dish_rating', models.FloatField()),
                ('dish_ingredients', models.ManyToManyField(to='dishes.Ingredients')),
                ('dish_povars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dishes.povar')),
            ],
        ),
    ]

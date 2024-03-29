# Generated by Django 3.0.7 on 2020-06-29 12:57

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('name_en', models.CharField(max_length=150, null=True)),
                ('name_ru', models.CharField(max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10000)),
                ('name_en', models.CharField(max_length=10000, null=True)),
                ('name_ru', models.CharField(max_length=10000, null=True)),
                ('image', models.CharField(blank=True, max_length=10000, null=True)),
                ('stars', models.FloatField(blank=True, default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('ingredients', models.TextField(blank=True, null=True)),
                ('ingredients_en', models.TextField(blank=True, null=True)),
                ('ingredients_ru', models.TextField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=50, null=True)),
                ('recipes', models.TextField()),
                ('recipes_en', models.TextField(null=True)),
                ('recipes_ru', models.TextField(null=True)),
                ('accessorizes', models.TextField()),
                ('accessorizes_en', models.TextField(null=True)),
                ('accessorizes_ru', models.TextField(null=True)),
                ('hint', models.TextField()),
                ('hint_en', models.TextField(null=True)),
                ('hint_ru', models.TextField(null=True)),
                ('model', models.CharField(blank=True, max_length=10000, null=True)),
                ('difficulty', models.CharField(blank=True, max_length=10000, null=True)),
                ('difficulty_en', models.CharField(blank=True, max_length=10000, null=True)),
                ('difficulty_ru', models.CharField(blank=True, max_length=10000, null=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food', to='core.Category')),
                ('category_en', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food', to='core.Category')),
                ('category_ru', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='food', to='core.Category')),
                ('cooked', models.ManyToManyField(blank=True, related_name='cooked', to=settings.AUTH_USER_MODEL)),
                ('favorite', models.ManyToManyField(blank=True, related_name='favorite', to=settings.AUTH_USER_MODEL)),
                ('shared', models.ManyToManyField(blank=True, related_name='shared', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

# Generated by Django 4.0 on 2022-01-02 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0002_alter_ingredient_options_ingredient_article_number_and_more'),
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ('name',), 'verbose_name': 'Recipe', 'verbose_name_plural': 'Recipes'},
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(through='recipes.RecipeIngredient', to='ingredients.Ingredient', verbose_name='Recipe ingredients'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=256, verbose_name='Recipe name'),
        ),
    ]
# Generated by Django 4.0.8 on 2022-10-31 10:18

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='cta_1',
        ),
        migrations.CreateModel(
            name='HomeCtaOneRelationship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('cta_one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cta_one_home_relationship', to='base.homectasection')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_cta_one_relationship', to='base.homepage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]

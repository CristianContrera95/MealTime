# Generated by Django 3.0.8 on 2021-06-02 00:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('meal_delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Creado')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Actualizado')),
                ('customizations', models.CharField(blank=True, error_messages={'blank': "The customizations field can't be blank.", 'invalid': 'The customizations field is invalid.', 'max_length': 'The customizations field must be at most 255 characters.', 'null': "The customizations field can't be null."}, max_length=255, null=True, verbose_name='Specify customizations')),
                ('menu_item', models.ForeignKey(error_messages={'blank': "The menu_item field can't be blank.", 'invalid': 'The menu_item field is invalid.', 'null': "The menu_item field can't be null."}, on_delete=django.db.models.deletion.CASCADE, to='meal_delivery.MenuItem', verbose_name='Menu Item')),
            ],
            options={
                'verbose_name': 'Order',
                'verbose_name_plural': 'Orders',
                'db_table': 'order',
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]

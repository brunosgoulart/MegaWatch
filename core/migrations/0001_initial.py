# Generated by Django 5.0.3 on 2024-04-30 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HDPO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PowerActive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PowerReactive', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Level', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
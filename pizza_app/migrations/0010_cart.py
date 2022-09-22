# Generated by Django 4.0.5 on 2022-06-29 12:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_app', '0009_alter_menu_pizza_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza_app.customer')),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza_app.menu')),
            ],
        ),
    ]

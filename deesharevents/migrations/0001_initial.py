# Generated by Django 5.0.4 on 2024-04-19 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='deesharevents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue', models.CharField(choices=[('Dublin 08', 'Dublin 08'), ('Dublin 10', 'Dublin 10')], max_length=100)),
                ('image', models.ImageField(upload_to='event_images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('alcoholic', models.BooleanField(default=False)),
                ('select_date', models.DateField()),
                ('expected_guests', models.IntegerField(default=0)),
            ],
        ),
    ]

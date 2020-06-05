# Generated by Django 3.0.6 on 2020-06-05 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dealers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('views', models.PositiveIntegerField(default=0, editable=False)),
                ('slug', models.SlugField(max_length=75)),
                ('number', models.CharField(max_length=16, unique=True)),
                ('status', models.CharField(blank=True, choices=[('pending', 'Pending'), ('published', 'Published'), ('sold', 'Sold'), ('archived', 'Archived')], default='pending', max_length=15)),
                ('extra_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Title second part')),
                ('engine_power', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('doors', models.PositiveSmallIntegerField(default=4)),
                ('sitting_places', models.PositiveSmallIntegerField(default=4)),
                ('first_registration_date', models.DateField(null=True)),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='CarBrand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('logo', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Car brand',
                'verbose_name_plural': 'Car brands',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CarEngine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name': 'Engine Type',
                'verbose_name_plural': 'Engine Types',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
            options={
                'verbose_name': 'Car model',
                'verbose_name_plural': 'Car models',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CarProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
            ],
            options={
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='FuelType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, unique=True)),
            ],
            options={
                'verbose_name': 'Fuel Type',
                'verbose_name_plural': 'Fuel Types',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, unique=True)),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='color',
            index=models.Index(fields=['name'], name='cars_color_name_95ff05_idx'),
        ),
        migrations.AddField(
            model_name='carproperty',
            name='car',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cars.Car'),
        ),
        migrations.AddField(
            model_name='carproperty',
            name='property',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cars.Property'),
        ),
        migrations.AddField(
            model_name='carmodel',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cars.CarBrand'),
        ),
        migrations.AddIndex(
            model_name='carengine',
            index=models.Index(fields=['name'], name='cars_careng_name_1f7da2_idx'),
        ),
        migrations.AddIndex(
            model_name='carbrand',
            index=models.Index(fields=['name'], name='cars_carbra_name_e5d8f6_idx'),
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.Color'),
        ),
        migrations.AddField(
            model_name='car',
            name='dealer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='dealers.Dealer'),
        ),
        migrations.AddField(
            model_name='car',
            name='engine_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.CarEngine'),
        ),
        migrations.AddField(
            model_name='car',
            name='fuel_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.FuelType'),
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cars.CarModel'),
        ),
        migrations.AddIndex(
            model_name='carmodel',
            index=models.Index(fields=['name'], name='cars_carmod_name_ef19d7_idx'),
        ),
        migrations.AddIndex(
            model_name='car',
            index=models.Index(fields=['status'], name='cars_car_status_3b4442_idx'),
        ),
    ]

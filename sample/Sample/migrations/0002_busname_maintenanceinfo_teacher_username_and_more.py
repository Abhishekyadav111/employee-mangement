# Generated by Django 4.0.4 on 2022-05-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sample', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='busname',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('busno', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='maintenanceinfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('drivename', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('busno', models.CharField(max_length=70)),
                ('foltpartname', models.CharField(max_length=70)),
                ('phone', models.IntegerField()),
                ('Rs', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('teacheridnamber', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=5)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='username',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('studentcardnumber', models.CharField(max_length=70)),
                ('email', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=5)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='employee',
            name='bonus',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='dept',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='role',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary',
        ),
        migrations.AddField(
            model_name='employee',
            name='employeeidnamber',
            field=models.CharField(default='ram', max_length=70),
        ),
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.CharField(max_length=5),
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
    ]
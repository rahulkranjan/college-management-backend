# Generated by Django 3.0.8 on 2020-12-20 10:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'profile',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.PositiveSmallIntegerField(choices=[(1, 'is_superadmin'), (2, 'is_admin'), (3, 'is_learner'), (4, 'is_instructor')], primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, choices=[('IS_SUPERADMIN', 'is_superadmin'), ('IS_ADMIN', 'is_admin'), ('IS_LEARNER', 'is_learner'), ('IS_INSTRUCTOR', 'is_instructor')], max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=100, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=40)),
                ('avtar', models.ImageField(blank=True, default='', upload_to='avtar/')),
                ('cover', models.ImageField(blank=True, default='', upload_to='cover/')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('contact', models.BigIntegerField(default=0, unique=True)),
                ('facebook', models.URLField(blank=True, default='')),
                ('linkdin', models.URLField(blank=True, default='')),
                ('youtube', models.URLField(blank=True, default='')),
                ('website_url', models.URLField(blank=True, default='')),
                ('about', models.TextField(blank=True, default='')),
                ('short_info', models.CharField(blank=True, default='', max_length=120)),
                ('education', models.TextField(blank=True, default='')),
                ('region', models.CharField(blank=True, default='', max_length=100)),
                ('achivements', models.CharField(blank=True, default='', max_length=500)),
                ('expertise_in', models.CharField(blank=True, default='', max_length=500)),
                ('popular', models.BooleanField(default=False)),
                ('visible_home', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('profile', models.ManyToManyField(blank=True, to='users.Profile')),
                ('roles', models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='users.Role')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

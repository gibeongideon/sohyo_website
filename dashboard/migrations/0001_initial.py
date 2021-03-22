# Generated by Django 3.1.7 on 2021-05-09 18:53

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(blank=True, max_length=2000, null=True, upload_to='images/%Y/%m/%d/')),
                ('description', models.TextField(blank=True, default='Soyo :Ensure Education For Every Poor Children', max_length=400, null=True)),
                ('donation_progress', models.FloatField(blank=True, null=True)),
                ('raised', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=12, null=True)),
                ('goal', models.DecimalField(blank=True, decimal_places=2, default=1, max_digits=12, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Common',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('mobile_no', models.CharField(blank=True, default='+254 722 259 264', max_length=100, null=True)),
                ('email', models.EmailField(blank=True, default='sohyo.sohyo@gmail.com', max_length=100, null=True)),
                ('address', models.CharField(blank=True, default='P O BoX 94 Mulot,Bomet ,Nairobi -Kenya', max_length=100, null=True)),
                ('newsletter', models.CharField(blank=True, default='Newsletter', max_length=300, null=True)),
                ('newsletter_dec', models.TextField(blank=True, default='Subsctibe to our newsletter to get updated             on our current events.We love seeing around.', max_length=300, null=True)),
                ('twitter', models.URLField(blank=True, default='http://www.twitter.com/', max_length=100, null=True)),
                ('facebook', models.URLField(blank=True, default='https://www.facebook.com/', max_length=100, null=True)),
                ('instagram', models.URLField(blank=True, default='http://www.instagram.com/', max_length=100, null=True)),
                ('youtube', models.URLField(blank=True, default='http://www.youtube.com/', max_length=100, null=True)),
                ('linkedin', models.URLField(blank=True, default='http://www.linkedin.com/', max_length=100, null=True)),
                ('google_plus', models.URLField(blank=True, default='http://www.google_plus.com/', max_length=100, null=True)),
                ('disrict', models.CharField(blank=True, default='Nairobi', max_length=300, null=True)),
                ('street', models.CharField(blank=True, default='Mulot-Sunset , Kipsete BLD', max_length=300, null=True)),
                ('image', models.ImageField(blank=True, max_length=2000, null=True, upload_to='images/%Y/%m/%d/')),
                ('title', models.CharField(blank=True, default='Fit Druds', max_length=300, null=True)),
                ('startime', models.DateTimeField(blank=True, null=True)),
                ('endtime', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('venuetitle', models.CharField(blank=True, default='Bomet', max_length=300, null=True)),
                ('town', models.CharField(blank=True, default='Bomet', max_length=300, null=True)),
                ('donate', models.CharField(blank=True, default='Donate', max_length=100, null=True)),
                ('event_header', models.CharField(blank=True, default='We Arrange Many Social Events to promote our mission', max_length=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(blank=True, max_length=2000, null=True, upload_to='images/%Y/%m/%d/')),
                ('description', models.TextField(blank=True, default='We as Soyo Arrange Many Social Events For Charity Donations', max_length=400, null=True)),
                ('startime', models.DateTimeField(blank=True, null=True)),
                ('endtime', models.DateTimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('venuetitle', models.CharField(blank=True, default='Bomet', max_length=300, null=True)),
                ('town', models.CharField(blank=True, default='Bomet', max_length=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('message', models.TextField(blank=True, max_length=400, null=True)),
                ('full_name', models.CharField(blank=True, max_length=300, null=True)),
                ('email', models.EmailField(blank=True, max_length=300, null=True)),
                ('subject', models.CharField(blank=True, max_length=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(blank=True, max_length=2000, null=True, upload_to='images/%Y/%m/%d/')),
                ('name', models.TextField(blank=True, default='Jon Doe', max_length=200, null=True)),
                ('title', models.CharField(blank=True, default='Volunteer leader', max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('titleup', models.CharField(blank=True, default='Healthy,Developed', max_length=100, null=True)),
                ('titledown', models.CharField(blank=True, default='and focused community.', max_length=100, null=True)),
                ('small_description', models.TextField(blank=True, default='Vision: To Create a healhy and focused community.', max_length=200, null=True)),
                ('donate', models.CharField(blank=True, default='Donate', max_length=100, null=True)),
                ('mobile_no', models.CharField(blank=True, default='+254 722 259 264', max_length=100, null=True)),
                ('email', models.EmailField(blank=True, default='sohyo.sohyo@gmail.com', max_length=100, null=True)),
                ('address', models.CharField(blank=True, default='P O BoX 94 Mulot,Bomet', max_length=100, null=True)),
                ('what_we_are_doing', models.CharField(blank=True, default='Our Mission', max_length=300, null=True)),
                ('mission1', models.CharField(blank=True, default="Protect Youth's Heath", max_length=300, null=True)),
                ('mission1_desc', models.TextField(blank=True, default="* Fight against drugs and substance abuse among the youth.* Promote youth 's health  through reproductive education & HIV/AIDS awareness.* Guidance & counselling to the youth.", max_length=300, null=True)),
                ('mission2', models.CharField(blank=True, default='Promote Career,Talent & Skills', max_length=300, null=True)),
                ('mission2_desc', models.TextField(blank=True, default='*Promote capacity building on entrepreneurship skills .*Empowers and enhance leadership skills', max_length=300, null=True)),
                ('mission4', models.CharField(blank=True, default='Environmental Conservation', max_length=300, null=True)),
                ('mission4_desc', models.TextField(blank=True, default='*Planting trees in public places which include schools,churches etc.', max_length=300, null=True)),
                ('about_our_foundation_header', models.CharField(blank=True, default='About the Organization', max_length=300, null=True)),
                ('about_our_foundation_sub_header', models.CharField(blank=True, default='Our Mission', max_length=300, null=True)),
                ('about_our_foundation_desc1', models.TextField(blank=True, default='To equip the young people with life skills and impact knowledge to promote health and development in achieving their full physical ,intellectual,morals and social potential as members of the community.', max_length=300, null=True)),
                ('about_our_foundation_desc2', models.TextField(blank=True, default='', max_length=300, null=True)),
                ('exlore_causes', models.CharField(blank=True, default='Explore Our Latest Causes', max_length=300, null=True)),
                ('events_plans', models.CharField(blank=True, default='We arrange many social events for charity', max_length=300, null=True)),
                ('dev_mobile', models.CharField(blank=True, default='-0712 478 566', max_length=300, null=True)),
                ('change', models.CharField(blank=True, default='At SOHYO We Serve To Save', max_length=300, null=True)),
                ('active', models.BooleanField(blank=True, default=False, null=True)),
                ('about1_image', models.ImageField(blank=True, max_length=2000, null=True, upload_to='images/%Y/%m/%d/')),
                ('about2_image', models.ImageField(blank=True, max_length=2000, null=True, upload_to='images/%Y/%m/%d/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('value', models.FloatField(default=0)),
                ('type', models.CharField(blank=True, default='Donation', max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Testimomial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('image', models.ImageField(blank=True, max_length=2000, null=True, upload_to='images/%Y/%m/%d/')),
                ('name', models.CharField(blank=True, default="Gama'liel", max_length=200, null=True)),
                ('title', models.CharField(blank=True, default='CEO', max_length=100, null=True)),
                ('description', models.TextField(blank=True, default='“Stop asking what the country can do  for you ,instead ask what you can do for the country for a better tomorrow.” am at an age where I just want to be fit and healthy our bodies are our responsibility!”', max_length=300, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('member_type', models.CharField(blank=True, choices=[('Member', 'member'), ('Sponser', 'sponser'), ('Volunteer', 'volunteer'), ('Others', 'others')], default='Member', max_length=20, null=True)),
                ('others', models.CharField(blank=True, help_text='If others specify here', max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=150, null=True)),
                ('active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]

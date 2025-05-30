# Generated by Django 5.0.7 on 2025-05-05 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_category_tag_alter_blogpost_content_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NarrativePrediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('narrative_type', models.CharField(choices=[('displayed', 'Displayed Narrative'), ('hidden', 'Hidden Thread')], max_length=20)),
                ('prediction', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('fulfilled', 'Fulfilled'), ('failed', 'Failed')], default='pending', max_length=20)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('outcome_notes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]

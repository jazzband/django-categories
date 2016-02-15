# -*- coding: utf-8 -*-


from django.db import models, migrations
import django.core.files.storage
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', models.SlugField(verbose_name='slug')),
                ('active', models.BooleanField(default=True, verbose_name='active')),
                ('thumbnail', models.FileField(storage=django.core.files.storage.FileSystemStorage(), null=True, upload_to='uploads/categories/thumbnails', blank=True)),
                ('thumbnail_width', models.IntegerField(null=True, blank=True)),
                ('thumbnail_height', models.IntegerField(null=True, blank=True)),
                ('order', models.IntegerField(default=0)),
                ('alternate_title', models.CharField(default='', help_text='An alternative title to use on pages with this category.', max_length=100, blank=True)),
                ('alternate_url', models.CharField(help_text='An alternative URL to use instead of the one derived from the category hierarchy.', max_length=200, blank=True)),
                ('description', models.TextField(null=True, blank=True)),
                ('meta_keywords', models.CharField(default='', help_text='Comma-separated keywords for search engines.', max_length=255, blank=True)),
                ('meta_extra', models.TextField(default='', help_text='(Advanced) Any additional HTML to be placed verbatim in the &lt;head&gt;', blank=True)),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(related_name='children', verbose_name='parent', blank=True, to='categories.Category', null=True)),
            ],
            options={
                'ordering': ('tree_id', 'lft'),
                'abstract': False,
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='CategoryRelation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.PositiveIntegerField(verbose_name='object id')),
                ('relation_type', models.CharField(help_text="A generic text field to tag a relation, like 'leadphoto'.", max_length='200', null=True, verbose_name='relation type', blank=True)),
                ('category', models.ForeignKey(verbose_name='category', to='categories.Category')),
                ('content_type', models.ForeignKey(verbose_name='content type', to='contenttypes.ContentType')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('parent', 'name')]),
        ),
    ]

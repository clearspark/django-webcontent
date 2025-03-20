from django.db import migrations

def set_public_content(apps, schema_editor):
    Content = apps.get_model('WebContent', 'Content')
    Group = apps.get_model('auth', 'Group')
    
    # Get the "everyone" group
    everyone_group = Group.objects.filter(name='everyone').first()
    if everyone_group:
        # Set is_public=True for all content that has the "everyone" group
        Content.objects.filter(authGroup=everyone_group).update(is_public=True)

def reverse_public_content(apps, schema_editor):
    Content = apps.get_model('WebContent', 'Content')
    Group = apps.get_model('auth', 'Group')
    
    # Get or create the "everyone" group
    everyone_group, created = Group.objects.get_or_create(name='everyone')
    
    # Add the "everyone" group to all public content
    for content in Content.objects.filter(is_public=True):
        content.authGroup.add(everyone_group)

class Migration(migrations.Migration):

    dependencies = [
        ('WebContent', '0008_content_is_public_alter_content_id_and_more'),
    ]

    operations = [
        migrations.RunPython(set_public_content, reverse_public_content),
    ] 
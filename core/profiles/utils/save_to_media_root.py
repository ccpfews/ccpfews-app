from django.conf import settings

# utility to save file to media root in chuck


def save_uploaded_file_to_media_root(f, file_name):
    with open('%s%s' % (settings.MEDIA_ROOT, file_name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

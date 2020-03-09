"""
parse and set up voters from uploaded voter files

DEPRECATED

Ben Adida
ben@adida.net
2010-05-22
"""

from django.core.management.base import BaseCommand

from helios.models import VoterFile


class Command(BaseCommand):
    args = ''
    help = 'load up voters from unprocessed voter files'

    def handle(self, *args, **options):
        # load up the voter files in order of last uploaded
        files_to_process = VoterFile.objects.filter(processing_started_at=None).order_by('uploaded_at')

        for file_to_process in files_to_process:
            file_to_process.process()

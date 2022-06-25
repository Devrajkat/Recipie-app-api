"""
Django command to wait fo the database to be available.
"""
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg20Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    """ Django command to wait for the database"""

    def handle(self, *args, **options):
        """ Entrypoint for command """
        self.stdout.write('Waiting for database')  # stdout is standard output
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg20Error, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second ...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available'))

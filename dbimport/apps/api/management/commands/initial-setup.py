import json
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from dbimport.apps.api.models import Location

class Command(BaseCommand):
    help = 'Import locations from a JSON file into the database'

    def handle(self, *args, **options):
        json_file_path = getattr(settings, "IMPORT_FILE_LOCATION")
        if not json_file_path:
            raise ValueError("Please provide the path to the file using setting.IMPORT_FILE_LOCATION.")

        with open(json_file_path, 'r') as file:
            data = json.load(file)

        # Fetch existing entries from the database
        existing_codes = set(Location.objects.values_list('unloc_code', flat=True))

        batch_size = getattr(settings, "IMPORT_BATCH_SIZE", 100)

        batch = []
        batch_count = 0

        # Skip existing entries and run a bulk create query for the whole batch
        for unloc_code, details in data.items():
            if unloc_code not in existing_codes:
                batch.append(
                    Location(
                        unloc_code=unloc_code,
                        code=details.get("code"),
                        name=details.get('name'),
                        city=details.get('city'),
                        country=details.get('country'),
                        province=details.get('province'),
                        timezone=details.get('timezone'),
                        coordinates=details.get('coordinates', []),
                        alias=details.get('alias', []),
                        unlocs=details.get('unlocs', []),
                        regions=details.get('regions', []),
                    )
                )

                # If the batch is full, insert it into the database
                if len(batch) >= batch_size:
                    Location.objects.bulk_create(batch)
                    batch_count += 1
                    self.stdout.write(self.style.SUCCESS(f'Inserted batch {batch_count}'))
                    batch = []  # Reset the batch

        # Insert any remaining records in the last batch
        if batch:
            Location.objects.bulk_create(batch)
            batch_count += 1
            self.stdout.write(self.style.SUCCESS(f'Inserted batch {batch_count}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully imported {len(data) - len(existing_codes)} new locations in {batch_count} batches'))


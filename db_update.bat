manage.py dumpdata workshop --indent=4 > workshop/fixtures/initial_data.json
manage.py flush
manage.py syncdb
manage.py loaddata workshop/fixtures/initial_data.json

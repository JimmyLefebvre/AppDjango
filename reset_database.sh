#!/bin/bash

echo "Deleting database files in progress ..."
for filename in $PWD/*/migrations/*.py; do
    if [[ ! $filename =~ .*?__init__.py ]]; then rm -f $filename; fi
done
rm -f db.sqlite3
echo "The database was erased with success !"

read -p "Do you want to create a new clean database? [Y/N]" -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]
then
    echo "Migrations in progress ..."
    python manage.py makemigrations
    echo "Migrate in progress ..."
    python manage.py migrate
fi

echo "It's done !"
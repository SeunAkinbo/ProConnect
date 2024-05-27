#!/bin/bash

# Database credentials
USER="pro_dev"
PASSWORD="pro_dev_pwd"
HOST="18.234.105.208"
DB_NAME="pro_dev_db"

# SQL file
SQL_FILE="decoy_profiles.sql"

# Import the dump file
mysql -u $USER -p$PASSWORD -h $HOST $DB_NAME < $SQL_FILE

echo "Data imported successfully."

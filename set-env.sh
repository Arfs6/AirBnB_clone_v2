#!/usr/bin/env bash
# Toggle between file storage and database storage.
export HBNB_MYSQL_USER="hbnb_dev"
export HBNB_MYSQL_PWD="hbnb_dev_pwd"
export HBNB_MYSQL_DB="hbnb_dev_db"
export HBNB_MYSQL_HOST="localhost"
if [ ! -n "${HBNB_TYPE_STORAGE:-}" ]; then
	echo "storage set to db"
	export HBNB_TYPE_STORAGE="db"
else
	echo "storage type not set"
	unset HBNB_TYPE_STORAGE
fi

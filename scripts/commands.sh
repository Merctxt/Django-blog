#!/bin/sh

set -e

wait_psql.sh

collectstatic.sh
makemigrations.sh
migrate.sh
runserver.sh
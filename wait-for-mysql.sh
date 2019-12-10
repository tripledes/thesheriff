#!/bin/sh
# wait-for-postgres.sh

set -e

cmd="$@"

until mysqladmin ping -h db -u sheriff -psh3r1ff; do
  >&2 echo "MariaDB is unavailable - sleeping"
  sleep 1
done

>&2 echo "MariaDB is up - executing command"
exec $cmd
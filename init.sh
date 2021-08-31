#!/bin/bash

export DB_NAME="nlp"
export DB_USER="nlp"
export DB_PASSWORD="top_secret"
export DB_HOST="localhost"
export DB_PORT="12345"

export DB_DOCKER_NAME="nlp-db"

nlp_kill_db() {
    [ "$(docker ps -a | grep $DB_DOCKER_NAME)" ] && docker kill $DB_DOCKER_NAME
}

nlp_start_db() {
    [ ! "$(docker ps -a | grep $DB_DOCKER_NAME)" ] &&
        docker run --rm -d -p $DB_PORT:5432 \
            -e POSTGRES_PASSWORD=$DB_PASSWORD \
            -e POSTGRES_USER=$DB_USER \
            -e POSTGRES_DB=$DB_NAME --name $DB_DOCKER_NAME postgres:12

    until psql 'postgres://'$DB_USER':'$DB_PASSWORD'@'$DB_HOST':'$DB_PORT'/'$DB_NAME \
        -c 'select 1' >/dev/null 2>&1; do
        echo 'CONNECTING ...'
        sleep 1s
    done
}

nlp_restart_db() {
    nlp_kill_db
    nlp_start_db
}

nlp_main() {
    echo "Starting database service"
    nlp_start_db
    echo "ALL DONE!"
}

nlp_shutdown() {
    nlp_kill_db
    tmux kill-session -t nlp
}

nlp_main

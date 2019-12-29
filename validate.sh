#!/usr/bin/env bash

set -euo pipefail

DOCKER_COMPOSE=""
MAKE=""
CURL=""

die() {
    # Print in RED
    printf "\e[31m[ERROR] ==> Failed %s \e[0m\n" "${1:-'unknown'}"
    exit 1
}

info() {
    printf "\e[36m[INFO] ==> %s \e[0m\n" "${1:-'unknown'}"
}

preflight_checks() {
    DOCKER_COMPOSE="$(command -v docker-compose)"
    MAKE="$(command -v make)"
    CURL="$(command -v curl)"

    if [ ! -x "${DOCKER_COMPOSE}" ]; then
        die "could not find docker-compose in the PATH"
    fi

    if [ ! -x "${MAKE}" ]; then
        die "could not find make in the PATH"
    fi

    if [ ! -x "${CURL}" ]; then
        die "could not find curl in the PATH"
    fi
}

run_validation() {
    info "Starting up the application"
    ${DOCKER_COMPOSE} up -d --quiet-pull >/dev/null || die "starting the application"

    info "Waiting for the application to be available"
    while (! curl -s http://localhost:5000 >/dev/null 2>&1); do info "Still waiting..."; sleep 5s; done
    
    info "Application found, continuing..."
    info "Creating 3 Outlaws..."
    for outlaw in create_outlaw_1.json create_outlaw_2.json create_outlaw_3.json; do
        curl localhost:5000/api/v1/outlaw -s -X POST \
            --data @examples/json/${outlaw} \
            -H 'Content-Type: application/json'
        sleep 2
    done
    
    info "Creating 1 Gang..."
    curl localhost:5000/api/v1/gang -s -X POST \
        --data @examples/json/create_gang.json \
        -H 'Content-Type: application/json'
    sleep 2

    info "Creating 1 Raid..."
    curl http://localhost:5000/api/v1/raid -s -X POST \
        -H 'Content-Type: application/json' \
        --data @examples/json/create_raid.json
    sleep 2

    info "Rating the Raid by two Outlaws..."
    for outlaw_id in 2 3; do
        curl localhost:5000/api/v1/raid/1/rate -s -X PUT \
            --data @examples/json/rate_raid_outlaw_${outlaw_id}.json \
            -H 'Content-Type: application/json'
        sleep 2
    done

    info "Ending a Raid..."
    curl localhost:5000/api/v1/raid/1/end -s -X PUT -H 'Content-Type: application/json'
    sleep 2

    info "Listing all Gangs..."
    curl localhost:5000/api/v1/gang -s
    sleep 2

    info "Listing outlaw's Gangs..."
    curl localhost:5000/api/v1/outlaw/1/gangs -s
    sleep 2

    info "Inviting a friend..."
    curl localhost:5000/api/v1/outlaw/1/invite_friend -s \
        -X POST --data @examples/json/invite_friend.json \
        -H 'Content-Type: application/json'
    sleep 2
}

cleanup() {
    info "cleaning up ..."
    ${DOCKER_COMPOSE} down > /dev/null || true
    ${MAKE} purge || true
}

preflight_checks
run_validation
cleanup
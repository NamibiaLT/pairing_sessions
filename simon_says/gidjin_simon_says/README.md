# Requirments

Docker https://docs.docker.com/

## Optional

Docker sync https://docker-sync.readthedocs.io/

# Running code

>  docker-compose run --rm simon

# Development Run

Start the docker sync server

> docker-sync start

Run the game using local changes

> docker-compose -f docker-compose.yml -f docker-compose-dev.yml run --rm simon



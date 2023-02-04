Author: @ilsep93

Notes based on `data-engineering-zoomcamp` videos.

# Docker

Use the `--help` tag to get additional information on Docker commands. For example:

```bash
docker build --help
```

# Docker Images

Pull Python image tag 3.9 from Docker Hub

```bash
docker pull python:3.9
```

Confirm Python image exists

```bash
docker images
```

Run docker in interactive mode with terminal. The entrypoint indicates what program should be run when container is active. In this case, a bash terminal is opened.

```bash
docker run -it --entrypoint=bash python:3.9
```

# Using Networks

A network will allow two containers to interact with each other. In this case, we buld a network between postgresql and pgadmin.

First, build a network between pgadmin and postgres. The network is called `pg-network`

```bash
docker network create pg-network
```

A list of created networks can be obtained using `docker network ls`

Run PostGres container. The "e" flag passes environment variables.
We map a volume so the data persists after the container is stopped. Otherwise, all data would be deleted after the container stops.

```bash
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -v $(pwd)/ny_taxi_postgres_data:/var/lib/postgresql/data \
    -p 4000:5432 \
    --network=pg-network \
    --name pg-database \
    postgres:13

docker run -it \
    -e PGADMIN_DEFAULT_EMAIL="admin@admin.com" \
    -e PGADMIN_DEFAULT_PASSWORD="root" \
    -p 8080:80 \
    --network=pg-network \
    --name pg-admin \
    dpage/pgadmin4
```

## Connect to pgadmin

Bring up a broswer to localhost:8080 and log in with the credentials that you used.

* Right click on Servers > Register > Server
* General tab: Specify name
* Connection tab: 
  * Hostname: local run= localhost
  * Hostcame: inside network = name of postgres container
  * Port: 5432
  * Username: postgres -e username
  * Password: postgres -e password

# Docker Compose

We can run the two containers together in a single file using Docker compose (see `docker-compose.yaml`)
 -d stands for detached mode (for access to terminal)
Remember to navigate to working directory with docker compose file

```bash
docker-compose up -d
```

Stopping the containers:

```bash
docker-compose down
```

# pgcli

Use pgcli to connect to Postgres using the terminal (no pgadmin).
This should be run while Docker container for postgres is still active.

```bash
docker pull postgres:13
```
Specify the required postgres environment variables and map port 5432 to 4000.

```bash
docker run -it \
    -e POSTGRES_USER="root" \
    -e POSTGRES_PASSWORD="root" \
    -e POSTGRES_DB="ny_taxi" \
    -p 4000:5432 \
    --name pg-database \
    postgres:13
```

```bash
pip install pgcli
```

```bash
pgcli --version
```

```bash
pgcli -h localhost -p 4000 -u root -d ny_taxi
```

# Dockerfile

A Dockerfile is used to build images. Here, we build an image with packages required to ingest our taxi data into postgres.

Specify which Dockerfile should be run by using -f (file) tag with the name and dot to signify current wd should be used for build context.

```bash
docker build -f Dockerfile . -t taxi_ingest:v001
```

# Ingest data to Postgres

## Locally

Note that the host is `localhost` when run locally, and the port is `4000`.


```bash
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz"

python hw_ingest_data.py \
        --user=root \
        --password=root \
        --host=localhost \
        --port=4000 \
        --db=ny_taxi \
        --table_name=green_taxi_trips \
        --url=${URL}
```

## Dockerized

To run `hw_ingest_data.py` on a Docker container, make sure that a postgres container is active.
Change the `host` to the name of the container running postgres, and change the port to `5432`.

We use the image that was built using the Dockerfile.

*green taxi data*:

```bash
URL="https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2019-01.csv.gz"

docker run -it \
--network=pg-network \
 taxi_ingest:v001 \
        --user=root \
        --password=root \
        --host=pg-database \
        --port=5432 \
        --db=ny_taxi \
        --table_name=green_taxi_trips \
        --url=${URL}
```

*zones*:

```bash
URL="https://s3.amazonaws.com/nyc-tlc/misc/taxi+_zone_lookup.csv"

docker run -it \
  --network=pg-network \
  taxi_ingest:v001 \
    --user=root \
    --password=root \
    --host=pg-database \
    --port=5432 \
    --db=ny_taxi \
    --table_name=zones \
    --url=${URL}
```

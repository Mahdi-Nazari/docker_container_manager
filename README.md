# Docker Container Manager RESTAPI

A Django project for the Docker Engine API. It lets you to manage your `docker` containers from within Python apps – run containers, update containers, delete containers, etc.

**I have tried to handle all of the operations by my self and not to use premade tools like class based views, database operations and etc.**

## Endpoints

Endpoints for viewing and manipulating the Containers.

* [Get container list](docs/list.md) : `GET /container/all/`
* [Get container info](docs/info.md) : `GET /container/single/:name/`
* [Get container logs](docs/logs.md) : `GET /container/logs/:name/`
* [Create container](docs/create.md) : `POST /container/create/`
* [Create multiple container from running container](docs/create_multiple.md) : `POST /container/create/multiple/:name/`
* [Update container](docs/update.md) : `PUT /container/update/:name/`
* [Delete container](docs/delete.md) : `DELETE /container/delete/:name/`
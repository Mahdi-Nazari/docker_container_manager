# Update Container

Update the Container with the needed information like `image`, `envs` and `command`.

**URL** : `/container/update/:name/`

**Query Parameters** : `name=[string]` where `name` is the Name of the Container on your machine.

**Method** : `PUT`

**Auth required** : NO

**Data constraints**

Provide Container `name` without any changes.

```json
{
    "name": "[unicode 255 chars max]",
    "image": "[unicode 255 chars max]",
    "envs": {"key", "value"},
    "command": "[unicode 255 chars max]"
}
```

**Data example** Partial data is allowed, but not for `name` field.

```json
{
    "name": "python",
    "image": "python:latest",
    "envs": {},
    "command": "uvicorn main:app",
}
```

## Success Responses

**Condition** : Update can be performed either fully or partially based on data, if container `name` is not changed.

**Code** : `200 OK`

**Content example** : For the example above, `image` is updated.

```json
{
    "name": "python",
    "image": "python:latest",
    "envs": {},
    "command": "uvicorn main:app",
    "state": "Running",
    "last_update": "2023-09-25T20:36:06.503464Z",
    "created_at": "2023-09-25T14:21:06.503576Z"
}
```

## Error Response

**Condition** : If Container does not exist.

**Code** : `404 NOT FOUND`

**Content** : `{}`

### Or

**Condition** : Container name is changed.

**Code** : `400 BAD REQUEST`

**Content** :

```json
{
    "Can not Update name of the container."
}
```

## Notes

### Data ignored

Endpoint will ignore `image`, `envs`, `command` if they dose not have new value.

**Data example**

```json
{
    "name": "python",
    "image": "python:3.11-slim-bookworm",
}
```

**Code** : `200 OK`

**Content example**

```json
{
    "name": "python",
    "image": "python:3.11-slim-bookworm",
    "envs": {},
    "command": "uvicorn main:app",
    "state": "Running",
    "last_update": "2023-09-25T20:36:06.503464Z",
    "created_at": "2023-09-25T14:21:06.503576Z"
}
```

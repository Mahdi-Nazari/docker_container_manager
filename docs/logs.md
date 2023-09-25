# Get Container Logs

Get the list of a container logs along the information that was run with it each time.

**URL** : `/container/logs/:name/`

**Query Parameters** : `name=[string]` where `name` is the Name of the Container on your machine.

**Method** : `GET`

**Auth required** : NO

Data : `{}`

## Success Response

**Code** : `200 OK`

**Content**

```json
[
    {
        "name": "python",
        "image": "python:3.11-alpine",
        "envs": {},
        "command": "python --version",
        "state": "Finished",
        "action": "Deleted",
        "created_at": "2023-09-25T15:11:27.305405Z"
    },
    {
        "name": "python",
        "image": "python:3.11-alpine",
        "envs": {},
        "command": "python --version",
        "state": "Finished",
        "action": "Updated",
        "created_at": "2023-09-25T14:36:43.305405Z"
    },
    {
        "name": "python",
        "image": "python",
        "envs": {},
        "command": "uvicorn main:app",
        "state": "Running",
        "action": "Created",
        "created_at": "2023-09-25T14:07:50.953972Z"
    }
]
```

## Error Responses

**Condition** : If Container does not exist with `name` of provided `name` parameter.

**Code** : `404 NOT FOUND`

**Content** : `{}`
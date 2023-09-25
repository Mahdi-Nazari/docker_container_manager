# Get Container List

Get the list of containers along their information.

**URL** : `/container/all/`

**Method** : `GET`

**Auth required** : NO

Data : `{}`

## Success Response

**Code** : `200 OK`

**Content**

A list of containers with the information that it was run with.

```json
[
    {
        "name": "mysql",
        "image": "mysql",
        "envs": {
            "MYSQL_ROOT_PASSWORD": "password"
        },
        "command": "",
        "state": "Finished",
        "last_update": "2023-09-25T14:21:06.503464Z",
        "created_at": "2023-09-25T14:21:06.503576Z"
    },
    {
        "name": "nginx",
        "image": "nginx",
        "envs": {},
        "command": "sleep 1000",
        "state": "Running",
        "last_update": "2023-09-25T14:21:05.175930Z",
        "created_at": "2023-09-25T14:21:05.176039Z"
    }
]
```

# Get Container List With State

Get the list of containers along their information based on container state.

**URL** : `/container/all/?state=/`

**Query Parameters** : `state=[string]` where `state` is the State of the Container on your machine.

**Method** : `GET`

**Auth required** : NO

## Success Response

**Code** : `200 OK`

**Content examples**

A list of containers with **Running** state.

```json
[
    {
        "name": "nginx",
        "image": "nginx",
        "envs": {},
        "command": "sleep 1000",
        "state": "Running",
        "last_update": "2023-09-25T14:21:05.175930Z",
        "created_at": "2023-09-25T14:21:05.176039Z"
    }
]
```

A list of containers with **Finished** state.

```json
[
    {
        "name": "mysql",
        "image": "mysql",
        "envs": {
            "MYSQL_ROOT_PASSWORD": "password"
        },
        "command": "",
        "state": "Finished",
        "last_update": "2023-09-25T14:21:06.503464Z",
        "created_at": "2023-09-25T14:21:06.503576Z"
    }
]
```

## Error Responses

**Condition** : If state parameters is wrong.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "Unsupported state Type."
}
```
# Get Container Info

Get the information.

**URL** : `/container/single/:name/`

**Query Parameters** : `name=[string]` where `name` is the Name of the Container on your machine.

**Method** : `GET`

**Auth required** : NO

**Data**: `{}`

## Success Response

**Code** : `200 OK`

**Content example**

```json
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
```

## Error Responses

**Condition** : If Container does not exist with `name` of provided `name` parameter.

**Code** : `404 NOT FOUND`

**Content** : `{}`
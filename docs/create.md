# Create Container

Run Container if a Container with that Name does
not already exist.

**URL** : `/container/create/`

**Method** : `POST`

**Auth required** : NO

**Data constraints**

Provide `name` and `image` of Container to be created.

```json
{
    "name": "[unicode 255 chars max]",
    "image": "[unicode 255 chars max]"
}
```

**Data example** name and image fields must be sent, other is optional.

```json
{
    "name": "mysql",
    "image": "mysql",
    "envs": {"MYSQL_ROOT_PASSWORD": "password"},
    "command": "sleep 1000"
}
```

## Success Response

**Condition** : If everything is OK and an Container with that name didn't exist.

**Code** : `201 CREATED`

**Content example**

```json
{
    "name": "mysql",
    "image": "mysql",
    "envs": {
        "MYSQL_ROOT_PASSWORD": "password"
    },
    "command": "sleep 10000",
    "state": "Running",
    "last_update": "2023-09-25T14:21:05.175930Z",
    "created_at": "2023-09-25T14:21:05.176039Z"
}
```

## Error Responses

**Condition** : If Container already exists.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "name": [
        "container with this name already exists."
    ]
}
```

### Or

**Condition** : If fields are missed.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "name": [
        "This field is required."
    ],
    "image": [
        "This field is required."
    ]
}
```

# Create Multiple Container From Running Container

Run Multiple instance of the Container if a Container with those Names does
not already exist.

**URL** : `/container/create/multiple/:name/`

**Query Parameters** : `name=[string]` where `name` is the Name of the Container on your machine that you want to run multiple instances from.

**Method** : `POST`

**Auth required** : NO

**Data constraints**

Provide `number` and `name_list` of Containers to be created.

```json
{
    "number": [integer min 1], 
    "name_list": ["[unicode 255 chars max]"]
}
```

**Data example** All fields must be sent.

```json
{
    "number": 3, 
    "name_list": ["mysql1", "mysql2","mysql3"]
}
```

## Success Response

**Condition** : If everything is OK and an Container with that names didn't exist.

**Code** : `201 CREATED`

**Content example**

```json
[
    "mysql1", "mysql2", "mysql3"
]
```

## Error Responses

**Condition** : If Container does not exist with `name` of provided `name` parameter.

**Code** : `404 NOT FOUND`

**Content** : `{}`

### Or

**Condition** : If `number` is not equal with length of `name_list`.

**Code** : `400 BAD REQUEST`

**Content example** :

```json
{
    "Number is not equal with length of Name list."
}
```

### Or

**Condition** : If Container already exists.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "Container with 'name' name is Already Exists."
}
```

### Or

**Condition** : If fields are missed.

**Code** : `400 BAD REQUEST`

**Content example**

```json
{
    "number": [
        "This field is required."
    ],
    "name_list": [
        "This field is required."
    ]
}
```

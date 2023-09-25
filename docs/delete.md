# Delete Container

Delete the Container.

**URL** : `/container/delete/:name/`

**Query Parameters** : `name=[string]` where `name` is the Name of the Container on your machine.

**Method** : `DELETE`

**Auth required** : NO

**Data** : `{}`

## Success Response

**Condition** : If the Container exists.

**Code** : `204 NO CONTENT`

**Content** : `{}`

## Error Responses

**Condition** : If Container does not exist with `name` of provided `name` parameter.

**Code** : `404 NOT FOUND`

**Content** : `{}`

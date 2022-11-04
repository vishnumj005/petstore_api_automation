ADD_PETS_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "photoUrls": {
      "type": "array",
      "items": [
        {
          "type": "string"
        }
      ]
    },
    "tags": {
      "type": "array",
      "items": {}
    },
    "status": {
      "type": "string"
    }
  },
  "required": [
    "id",
    "name",
    "photoUrls",
    "tags",
    "status"
  ]
}

DELETE_PETS_SCHEMA = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "code": {
      "type": "integer"
    },
    "type": {
      "type": "string"
    },
    "message": {
      "type": "string"
    }
  },
  "required": [
    "code",
    "type",
    "message"
  ]
}
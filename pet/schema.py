schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "received_date": {"type": "string", "pattern": "^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}Z$"}
    },
    "required": ["name", "received_date"]
}
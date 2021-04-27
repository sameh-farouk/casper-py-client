log_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "request": {"format": "--> %(message)s"},
        "response": {"format": "<-- (%(http_code)s %(http_reason)s) %(message)s"},
    },
    "handlers": {
        "request": {"formatter": "request", "class": "logging.StreamHandler"},
        "response": {"formatter": "response", "class": "logging.StreamHandler"},
    },
    "loggers": {
        "jsonrpcclient": {"level": "INFO"},
        "jsonrpcclient.client.request": {"handlers": ["request"]},
        "jsonrpcclient.client.response": {"handlers": ["response"]},
    },
}

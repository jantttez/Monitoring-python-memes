#!/bin/bash


gunicorn -w 4 -k uvicorn.workers.UvicornWorker web:app -b 0.0.0.0:8000
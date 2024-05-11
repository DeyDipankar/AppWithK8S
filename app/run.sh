#!/bin/bash

RUN uvicorn app.main:app --host="0.0.0.0" --port="8000"
#!/bin/bash

#Activate python
source ~/virtualPython/what-to-cook-backend/bin/activate

cd ~/Code/what-to-cook-backend

uvicorn main:app --host 0.0.0.0 --port 8000



#!/bin/bash

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install necessary dependencies
pip install --upgrade pip
pip install fastapi uvicorn sqlalchemy databases asyncpg

# Generate the requirements.txt file for dependency tracking
pip freeze > requirements.txt

# Run Alembic to apply database migrations
alembic upgrade head

# Seed the database with initial data
python seed.py
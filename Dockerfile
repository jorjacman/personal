FROM python:3.11.4-slim

# set working dir and copy files
WORKDIR /app
COPY . .

# install dependencies
RUN pip install fastapi pydantic

# set the envs
ENV APP_PORT 9001

# run the app
CMD uvicorn app:app --host 0.0.0.0 --port $APP_PORT

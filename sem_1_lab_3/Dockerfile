FROM python:3.10-alpine AS builder

WORKDIR /app/src

COPY requirements.txt /app/src
RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt

COPY . /app/src

ENTRYPOINT ["python3"]
CMD ["main.py"]

EXPOSE 5000
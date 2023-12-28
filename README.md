# finance-json-api

## Run Web Server

```bash
> docker-compose up -d
```

```bash
> http GET localhost:8000/salary
HTTP/1.1 200 OK
content-length: 79
content-type: application/json
date: Thu, 28 Dec 2023 23:15:57 GMT
server: uvicorn

{
    "company": "Ice Cream C&A",
    "date": "2023-12-24T00:00:00",
    "liquid_salary": 2000.0
}
```

## Run Tests

```bash
python3 -m pytest tests
```
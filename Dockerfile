FROM python:3.8.5-slim
# Python cannot be upgraded without fixing a libgeos error

WORKDIR /usr/src/app

LABEL maintainer="Milo van der Linden - https://www.tiltshiftapps.nl"

ENV BACKEND_CORS_ORIGINS_CSV "http://localhost,http://localhost:4200,http://localhost:3000,https://bewerkdemarkten.tiltshiftapps.nl"
ENV USERS '{"demo": "test12345"}'

RUN apt-get update && apt-get install -y \
    gcc postgresql-client libpq-dev git

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000
VOLUME ["/usr/src/app/data"]
CMD [ "./algorithmregister.sh" ]

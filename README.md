# Installing Dependencies
Create a **.env** file along the lines of:
```
SECRET_KEY=TEMPORARY_UNSAFE_KEY
DATABASE_URL=postgresql://bigboard:mypassword@localhost:5432/bigboard_db
```
## Postgres
```bash
# Installing via apt will automatically create a postgres user
sudo apt install postgresql postgresql-contrib
# Enter postgres shell as user postgres
sudo -u postgres psql
```

In postgres shell:
```sql
CREATE USER bigboard WITH PASSWORD 'mypassword';
CREATE DATABASE bigboard_db;
GRANT ALL PRIVILEGES ON DATABASE bigboard_db TO bigboard;
```

Exit postgres shell with **\q**. \
Edit **.env** file's **DATABASE_URL** key to match your user, password, and database name.

## Docker
```bash
sudo apt install docker.io
docker build -t bigboard-sandbox .
```

## CS50x Speller Distribution Code
```bash
wget https://cdn.cs50.net/2026/x/psets/5/speller.zip
unzip speller.zip
rm speller.zip
```
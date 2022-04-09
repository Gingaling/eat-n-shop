-- settings.sql
CREATE DATABASE eat_n_shop;
CREATE USER eat_n_shopuser WITH PASSWORD 'eat_n_shop';
GRANT ALL PRIVILEGES ON DATABASE eat_n_shop TO eat_n_shopuser;

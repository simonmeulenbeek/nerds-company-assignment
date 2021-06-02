DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS authcode;

CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    roles TEXT,
    scopes TEXT
);

CREATE TABLE client (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id TEXT NOT NULL,
    client_secret TEXT,
    redirect_uri TEXT,
    scope TEXT,
    authorized_grant_types TEXT
);

CREATE TABLE authcode (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code TEXT NOT NULL,
    username TEXT NOT NULL,
    expiration TEXT
);
DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS client;

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
    client_secret TEXT NOT NULL,
    redirect_uri TEXT,
    scope TEXT,
    authorized_grant_types TEXT
);
CREATE SCHEMA wow;

CREATE TABLE wow.reports (
    code NCHAR(16) NOT NULL PRIMARY KEY,
    title TEXT,
    segments INTEGER,
    guild_id INTEGER,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    duration FLOAT
);

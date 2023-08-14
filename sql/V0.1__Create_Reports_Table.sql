CREATE TABLE reports (
    code NCHAR(16) NOT NULL PRIMARY KEY,
    title TEXT,
    segments INTEGER,
    guild_id INTEGER,
    start DATETIME,
    end DATETIME,
    duration DATETIME
);

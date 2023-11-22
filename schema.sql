CREATE TABLE pets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    photo_url TEXT,
    age INTEGER,
    notes TEXT,
    available BOOLEAN NOT NULL DEFAULT 1
);

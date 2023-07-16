CREATE TABLE IF NOT EXISTS beetles (
sn             INTEGER                  PRIMARY KEY,
date_collected TEXT                     NOT NULL,
trap_id        INTEGER                  NOT NULL,
sex text       CHECK(sex IN ('m', 'f')) NOT NULL,
CONSTRAINT timestamp CHECK (date_collected==strftime('%Y-%m-%d',date_collected))
);

CREATE TABLE IF NOT EXISTS mass (
sn        INTEGER NOT NULL,
mass      INTEGER NOT NULL,
time_stamp TEXT    UNIQUE,
CONSTRAINT timestamp CHECK (time_stamp==strftime('%Y-%m-%d %h:%m:%s',time_stamp)),
FOREIGN KEY (sn) REFERENCES beetles (sn)
);

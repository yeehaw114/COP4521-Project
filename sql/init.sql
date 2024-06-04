CREATE SEQUENCE wID
CREATE SEQUENCE sID

CREATE OR REPLACE FUNCTION genAlphaNum(num BIGINT)
RETURNS VARCHAR(255) AS $$

DECLARE 

    base_62 VARCHAR(62) := '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz';
    result VARCHAR(20) := '';
    remainder INTEGER;

BEGIN
    IF num = 0 THEN
        RETURN 0;
    END IF;

    WHILE num > 0 LOOP
        remainder := num % 62;
        result := substr(base_62, remainder + 1, 1) || result;
        num := num/62;
    END LOOP;

    RETURN result;
END;

$$ LANGUAGE plpgsql;

CREATE TABLE users {
    username VARCHAR(30) NOT NULL CHECK (username=LOWER(username)),
    password CHAR(60) NOT NULL,
    description VARCHAR(500) NOT NULL DEFAULT '',
    join_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY(username)
};

CREATE TABLE workouts {
    workoutID VARCHAR(10) NOT NULL DEFAULT genAlphaNum(NEXTVAL(wID)),
    name VARCHAR(50) NOT NULL DEFAULT '',
    username VARCHAR(30) NOT NULL,

    --Constraints
    CONSTRAINT fk_username FOREIGN KEY(username) REFERENCES users(username),

    PRIMARY KEY(workoutID)
}

CREATE TABLE sets {
    setID VARCHAR(10) NOT NULL DEFAULT genAlphaNum(NEXTVAL(sID)),
    workoutID VARCHAR(10) NOT NULL,
    reps SMALLINT NOT NULL DEFAULT 0,
    weight SMALLINT NOT NULL DEFAULT 0,

    --Constraints
    CONSTRAINT fk_workoutid FOREIGN KEY(workoutID) REFERENCES workouts(workoutID)

    PRIMARY KEY(setID)
}
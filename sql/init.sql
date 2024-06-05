CREATE SEQUENCE wID
CREATE SEQUENCE sID
CREATE SEQUENCE uwID

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

CREATE TABLE users (
    username VARCHAR(30) NOT NULL CHECK (username=LOWER(username)),
    password CHAR(60) NOT NULL,
    description VARCHAR(500) NOT NULL DEFAULT '',
    join_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY(username)
);

CREATE TABLE workouts (
    workout_id VARCHAR(10) NOT NULL DEFAULT genAlphaNum(NEXTVAL(wID)),
    name VARCHAR(50) NOT NULL DEFAULT '',
    username VARCHAR(30) NOT NULL,

    --Constraints
    CONSTRAINT fk_username FOREIGN KEY(username) REFERENCES users(username),

    PRIMARY KEY(workout_id)
);

CREATE TABLE exercises (
    name VARCHAR(30) NOT NULL,
    muscle_group VARCHAR(30) NOT NULL DEFAULT '',
    PRIMARY KEY(name)
);

--Table that maps many-many relationship between exercise and workout
CREATE TABLE workout_exercises (
    workout_id VARCHAR(10) NOT NULL,
    exercise_name VARCHAR(30) NOT NULL, 
    reps SMALLINT NOT NULL DEFAULT 0,
    weight SMALLINT NOT NULL DEFAULT 0,

    --Constraints
    CONSTRAINT fk_workoutid FOREIGN KEY(workout_id) REFERENCES workouts(workout_id),
    CONSTRAINT fk_exercise_name FOREIGN KEY(exercise_name) REFERENCES exercises(name),

    PRIMARY KEY(workout_id)
);


--Table that stores a user's workout along with a foreign key to the goal workout they were following
CREATE TABLE user_workouts(
    user_workout_id VARCHAR(10) NOT NULL DEFAULT genAlphaNum(NEXTVAL(uwID)),
    workoutID VARCHAR(10) NOT NULL,

    --Constraints
    CONSTRAINT fk_workoutid FOREIGN KEY(workoutID) REFERENCES workouts(workoutID)

    PRIMARY KEY(user_workout_id)
);
--Table that stores a user's individual sets of a particular workout
--which contains how many reps and how much weight they were able to do
CREATE TABLE user_sets(
    user_workout_id VARCHAR(10) NOT NULL,
    reps SMALLINT NOT NULL DEFAULT 0,
    weight SMALLINT NOT NULL DEFAULT 0,

    CONSTRAINT fk_user_workoutid FOREIGN KEY(user_workout_id) REFERENCES workouts(workoutID),

    PRIMARY KEY(user_workout_id)
);
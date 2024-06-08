CREATE SEQUENCE wID;
CREATE SEQUENCE uwID;
CREATE SEQUENCE usID;

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

CREATE TABLE workouts (
    id VARCHAR(10) NOT NULL DEFAULT genAlphaNum(NEXTVAL('wID')),
    name VARCHAR(50) NOT NULL DEFAULT '',
    username VARCHAR(30) NOT NULL,

    --Constraints
    CONSTRAINT fk_username FOREIGN KEY(username) REFERENCES auth_user(username),

    PRIMARY KEY(id)
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
    CONSTRAINT fk_workoutid FOREIGN KEY(workout_id) REFERENCES workouts(id),
    CONSTRAINT fk_exercise_name FOREIGN KEY(exercise_name) REFERENCES exercises(name),

    PRIMARY KEY(workout_id, exercise_name)
);


--Table that stores a user's workout along with a foreign key to the goal workout they were following
CREATE TABLE user_workouts(
    id VARCHAR(10) NOT NULL DEFAULT genAlphaNum(NEXTVAL('uwID')),
    workout_id VARCHAR(10) NOT NULL,
    username VARCHAR(30) NOT NULL,
    done_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    --Constraints
    CONSTRAINT fk_workoutid FOREIGN KEY(workout_id) REFERENCES workouts(id),
    CONSTRAINT fk_username FOREIGN KEY(username) REFERENCES auth_user(username),
    
    PRIMARY KEY(id)
);
--Table that stores a user's individual sets of a particular workout
--which contains how many reps and how much weight they were able to do
CREATE TABLE user_sets(
    id VARCHAR(10) NOT NULL DEFAULT genAlphaNum(NEXTVAL('usID')),
    workout_id VARCHAR(10) NOT NULL,
    exercise_name VARCHAR(30) NOT NULL,
    reps SMALLINT NOT NULL DEFAULT 0,
    weight SMALLINT NOT NULL DEFAULT 0,
    username VARCHAR(30) NOT NULL,

    --Constraints
    CONSTRAINT fk_exercise FOREIGN KEY(workout_id, exercise_name) REFERENCES workout_exercises(workout_id, exercise_name),
    CONSTRAINT fk_username FOREIGN KEY(username) REFERENCES auth_user(username),

    PRIMARY KEY(id)
);

--Role Based Access Roles
CREATE ROLE Administrator
GRANT ALL PRIVILEGES ON TABLE user_sets, user_workouts, workout_exercises, exercises, workouts, auth_user TO Administrator

CREATE ROLE Trainer
GRANT SELECT, INSERT, UPDATE ON TABLE workout_exercises, workouts, exercises TO Trainer

CREATE ROLE Trainee
GRANT SELECT, INSERT, UPDATE ON TABLE auth_user, user_workouts, user_sets TO Trainee
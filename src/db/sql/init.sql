use grpc;

CREATE TABLE user (
  user_id VARCHAR(10),
  user_name VARCHAR(20),
  password VARCHAR(16)
);

CREATE TABLE log (
  api_log VARCHAR(50),
  db_log VARCHAR(50),
  error VARCHAR(50)
);
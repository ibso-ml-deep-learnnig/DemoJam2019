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

CREATE TABLE asset (
  asset_id char(36) CHARACTER SET ascii COLLATE ascii_bin NOT NULL,
  asset_class char(8) NOT NULL,
  description text NOT NULL,
  picture char(50) NOT NULL,
  company_coe char(4) NOT NULL,
  asset_number char(12) NOT NULL,
  asset_subno char(4) NOT NULL,
  cost_center char(10) NOT NULL,
  acquisiton_date date NOT NULL,
  amount double unsigned zerofill NOT NULL,
  ul_year smallint(5) unsigned zerofill NOT NULL,
  ul_period smallint(5) unsigned zerofill NOT NULL,
  user_id char(10) NOT NULL,
  create_date date NOT NULL,
  create_time time NOT NULL
);

INSERT INTO user (user_id, user_name, password)
VALUES
('i333463',	'Eric Wu',	'123456'),
('admin',	'admin',	'admin');

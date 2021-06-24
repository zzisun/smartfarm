BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "users_users" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	"last_name"	varchar(150) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"email"	varchar(254) NOT NULL UNIQUE,
	"mobile_number"	varchar(12) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "users_users_groups" (
	"id"	integer NOT NULL,
	"users_id"	bigint NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("users_id") REFERENCES "users_users"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "users_users_user_permissions" (
	"id"	integer NOT NULL,
	"users_id"	bigint NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("users_id") REFERENCES "users_users"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "account_emailaddress" (
	"id"	integer NOT NULL,
	"email"	varchar(254) NOT NULL UNIQUE,
	"verified"	bool NOT NULL,
	"primary"	bool NOT NULL,
	"user_id"	bigint NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "users_users"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "account_emailconfirmation" (
	"id"	integer NOT NULL,
	"created"	datetime NOT NULL,
	"sent"	datetime,
	"key"	varchar(64) NOT NULL UNIQUE,
	"email_address_id"	bigint NOT NULL,
	FOREIGN KEY("email_address_id") REFERENCES "account_emailaddress"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	bigint NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	FOREIGN KEY("user_id") REFERENCES "users_users"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "device_management_device_info" (
	"device_serial"	integer NOT NULL,
	"device_model"	varchar(15) NOT NULL,
	"device_name"	varchar(15) NOT NULL,
	"device_detail"	varchar(100) NOT NULL,
	"device_ip_address"	varchar(40) NOT NULL,
	"device_password"	varchar(20) NOT NULL,
	"device_user_id"	bigint NOT NULL,
	FOREIGN KEY("device_user_id") REFERENCES "users_users"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("device_serial")
);
CREATE TABLE IF NOT EXISTS "device_management_mock_params" (
	"id"	integer NOT NULL,
	"serial"	varchar(15) NOT NULL,
	"ph"	real NOT NULL,
	"temp"	integer NOT NULL,
	"ec"	real NOT NULL,
	"nutrientA"	real NOT NULL,
	"light_lux"	integer NOT NULL,
	"date"	date NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "device_management_plant_info" (
	"id"	integer NOT NULL,
	"crop_group"	varchar(15) NOT NULL,
	"crop_name"	varchar(20),
	"life_stage"	varchar(15) NOT NULL,
	"planting_date"	date NOT NULL,
	"farm_info_id"	integer NOT NULL,
	FOREIGN KEY("farm_info_id") REFERENCES "device_management_farm_info"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "device_management_mock_interface" (
	"id"	integer NOT NULL,
	"cooler"	integer NOT NULL,
	"humidifier"	integer NOT NULL,
	"co2_gen"	integer NOT NULL,
	"air_pump"	integer NOT NULL,
	"device_info_id"	integer NOT NULL,
	FOREIGN KEY("device_info_id") REFERENCES "device_management_device_info"("device_serial") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "device_management_growth_params" (
	"id"	integer NOT NULL,
	"germination_time"	integer NOT NULL,
	"seeding_ec"	real NOT NULL,
	"ec"	real NOT NULL,
	"progress_date"	integer NOT NULL,
	"temparature"	integer NOT NULL,
	"ph"	real NOT NULL,
	"humidity"	real NOT NULL,
	"date"	date NOT NULL,
	"nutrientA"	real NOT NULL,
	"nutrientB"	real NOT NULL,
	"nutrientC"	real NOT NULL,
	"nutrientD"	real NOT NULL,
	"light_hr"	integer NOT NULL,
	"light_lux"	integer NOT NULL,
	"do"	real NOT NULL,
	"co2"	integer NOT NULL,
	"device_info_id"	integer NOT NULL,
	"plant_info_id"	bigint NOT NULL,
	FOREIGN KEY("device_info_id") REFERENCES "device_management_device_info"("device_serial") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("plant_info_id") REFERENCES "device_management_plant_info"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "django_site" (
	"id"	integer NOT NULL,
	"name"	varchar(50) NOT NULL,
	"domain"	varchar(100) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "socialaccount_socialapp_sites" (
	"id"	integer NOT NULL,
	"socialapp_id"	integer NOT NULL,
	"site_id"	integer NOT NULL,
	FOREIGN KEY("socialapp_id") REFERENCES "socialaccount_socialapp"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("site_id") REFERENCES "django_site"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "socialaccount_socialaccount" (
	"id"	integer NOT NULL,
	"provider"	varchar(30) NOT NULL,
	"uid"	varchar(191) NOT NULL,
	"last_login"	datetime NOT NULL,
	"date_joined"	datetime NOT NULL,
	"extra_data"	text NOT NULL,
	"user_id"	bigint NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "users_users"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "socialaccount_socialapp" (
	"id"	integer NOT NULL,
	"provider"	varchar(30) NOT NULL,
	"name"	varchar(40) NOT NULL,
	"client_id"	varchar(191) NOT NULL,
	"secret"	varchar(191) NOT NULL,
	"key"	varchar(191) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "socialaccount_socialtoken" (
	"id"	integer NOT NULL,
	"token"	text NOT NULL,
	"token_secret"	text NOT NULL,
	"expires_at"	datetime,
	"account_id"	bigint NOT NULL,
	"app_id"	bigint NOT NULL,
	FOREIGN KEY("account_id") REFERENCES "socialaccount_socialaccount"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("app_id") REFERENCES "socialaccount_socialapp"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "device_management_device_interface" (
	"id"	integer NOT NULL,
	"heater"	integer NOT NULL,
	"light"	integer NOT NULL,
	"pumpA"	integer NOT NULL,
	"pumpB"	integer NOT NULL,
	"pumpC"	integer NOT NULL,
	"pumpD"	integer NOT NULL,
	"pump_water"	integer NOT NULL,
	"air_pump"	integer NOT NULL,
	"cooler"	integer NOT NULL,
	"fan"	integer NOT NULL,
	"humidifier"	integer NOT NULL,
	"co2_gen"	integer NOT NULL,
	"device_info_id"	integer NOT NULL,
	"auto_air_contiditon_pump"	integer NOT NULL,
	"nut_pump_auto"	integer NOT NULL,
	"oxy_pump_auto"	integer NOT NULL,
	"water_pump_auto"	integer NOT NULL,
	FOREIGN KEY("device_info_id") REFERENCES "device_management_device_info"("device_serial") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "device_management_farm_info" (
	"id"	integer NOT NULL,
	"farm_type"	varchar(15) NOT NULL,
	"farm_capacity"	integer NOT NULL,
	"farm_plant_num"	integer NOT NULL,
	"farm_model_no"	varchar(15) NOT NULL,
	"device_info_id"	integer NOT NULL,
	"farm_name"	varchar(30) NOT NULL,
	FOREIGN KEY("device_info_id") REFERENCES "device_management_device_info"("device_serial") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "users_users_groups_users_id_group_id_02603a5e_uniq" ON "users_users_groups" (
	"users_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "users_users_groups_users_id_5572cf36" ON "users_users_groups" (
	"users_id"
);
CREATE INDEX IF NOT EXISTS "users_users_groups_group_id_3e15ff0f" ON "users_users_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "users_users_user_permissions_users_id_permission_id_119659d5_uniq" ON "users_users_user_permissions" (
	"users_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "users_users_user_permissions_users_id_04010ba6" ON "users_users_user_permissions" (
	"users_id"
);
CREATE INDEX IF NOT EXISTS "users_users_user_permissions_permission_id_9a117d64" ON "users_users_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "account_emailaddress_user_id_2c513194" ON "account_emailaddress" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "account_emailconfirmation_email_address_id_5b7f8c58" ON "account_emailconfirmation" (
	"email_address_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "device_management_device_info_device_user_id_5e6a792f" ON "device_management_device_info" (
	"device_user_id"
);
CREATE INDEX IF NOT EXISTS "device_management_plant_info_farm_info_id_136b7f68" ON "device_management_plant_info" (
	"farm_info_id"
);
CREATE INDEX IF NOT EXISTS "device_management_mock_interface_device_info_id_4a98d81c" ON "device_management_mock_interface" (
	"device_info_id"
);
CREATE INDEX IF NOT EXISTS "device_management_growth_params_device_info_id_450633ed" ON "device_management_growth_params" (
	"device_info_id"
);
CREATE INDEX IF NOT EXISTS "device_management_growth_params_plant_info_id_2b76e0a5" ON "device_management_growth_params" (
	"plant_info_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE UNIQUE INDEX IF NOT EXISTS "socialaccount_socialapp_sites_socialapp_id_site_id_71a9a768_uniq" ON "socialaccount_socialapp_sites" (
	"socialapp_id",
	"site_id"
);
CREATE INDEX IF NOT EXISTS "socialaccount_socialapp_sites_socialapp_id_97fb6e7d" ON "socialaccount_socialapp_sites" (
	"socialapp_id"
);
CREATE INDEX IF NOT EXISTS "socialaccount_socialapp_sites_site_id_2579dee5" ON "socialaccount_socialapp_sites" (
	"site_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "socialaccount_socialaccount_provider_uid_fc810c6e_uniq" ON "socialaccount_socialaccount" (
	"provider",
	"uid"
);
CREATE INDEX IF NOT EXISTS "socialaccount_socialaccount_user_id_8146e70c" ON "socialaccount_socialaccount" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "socialaccount_socialtoken_app_id_account_id_fca4e0ac_uniq" ON "socialaccount_socialtoken" (
	"app_id",
	"account_id"
);
CREATE INDEX IF NOT EXISTS "socialaccount_socialtoken_account_id_951f210e" ON "socialaccount_socialtoken" (
	"account_id"
);
CREATE INDEX IF NOT EXISTS "socialaccount_socialtoken_app_id_636a42d7" ON "socialaccount_socialtoken" (
	"app_id"
);
CREATE INDEX IF NOT EXISTS "device_management_device_interface_device_info_id_d350c8b2" ON "device_management_device_interface" (
	"device_info_id"
);
CREATE INDEX IF NOT EXISTS "device_management_farm_info_device_info_id_cdb8df71" ON "device_management_farm_info" (
	"device_info_id"
);
COMMIT;

create user postgraduate@'%' identified by 'yycx1996';
grant all privileges on EnglishArticalForPostgraduateExam.* to postgraduate@'%';
create database EnglishArticalForPostgraduateExam;

create table if not exists `Christian`(
	`id` INT UNSIGNED AUTO_INCREMENT,
	`href` VARCHAR(250) NOT NULL,
	`title` VARCHAR(250) NOT NULL,
	`content` TEXT NOT NULL,
	PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

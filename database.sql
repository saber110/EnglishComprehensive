create user postgraduate@'%' identified by 'yycx1996';
grant all privileges on EnglishArticalForPostgraduateExam.* to postgraduate@'%';
create database EnglishArticalForPostgraduateExam;

create table if not exists `Christian`(
	`id` INT UNSIGNED AUTO_INCREMENT,
	`href` VARCHAR(250) NOT NULL,
	`title` VARCHAR(250) NOT NULL,
	`content` TEXT NOT NULL,
	`time` TIMESTAMP NOT NULL,
	`sent` char,
	PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

create table if not exists `SpiderExcept`(
	`id` INT UNSIGNED AUTO_INCREMENT,
	`href` VARCHAR(250) NOT NULL,
	`except` TEXT NOT NULL,
	`time` TIMESTAMP NOT NULL,
	PRIMARY KEY(`id`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- create table if not exists `EmailSend`(
-- 	`id` INT UNSIGNED AUTO_INCREMENT,
-- 	`title` text NOT NULL,
-- 	`content` text not null,
-- 	`sent` char,
-- 	PRIMARY KEY(`id`)
-- )ENGINE=InnoDB DEFAULT CHARSET=utf8;

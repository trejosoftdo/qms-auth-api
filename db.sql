CREATE TABLE statuses (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `code` varchar(50) NOT NULL,
    `description` varchar(500) NOT NULL,
    `type` enum('CATEGORY','SERVICE','CUSTOMER','TURN','QUEUE') NOT NULL,
    `is_active` tinyint(1) NOT NULL DEFAULT '1',
    PRIMARY KEY (`id`)
)

CREATE TABLE priorities (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `code` varchar(50) NOT NULL,
    `description` varchar(500) NOT NULL,
    `is_active` tinyint(1) NOT NULL DEFAULT '1',
    PRIMARY KEY (`id`)
)

CREATE TABLE categories (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `code` varchar(50) NOT NULL,
    `description` varchar(500) NOT NULL,
    `icon_url` varchar(1024) NOT NULL,
    `is_active` tinyint(1) NOT NULL DEFAULT '1',
    `status_id` INTEGER NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY(`status_id`) REFERENCES `statuses` (`id`)
)

CREATE TABLE services (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(50) NOT NULL,
    `code` varchar(50) NOT NULL,
    `prefix` varchar(50) NOT NULL,
    `description` varchar(500) NOT NULL,
    `icon_url` varchar(1024) NOT NULL,
    `is_active` tinyint(1) NOT NULL DEFAULT '1',
    `status_id` INTEGER NOT NULL,
    `category_id` INTEGER NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY(`status_id`) REFERENCES `statuses` (`id`),
    FOREIGN KEY(`category_id`) REFERENCES `categories` (`id`)
)

CREATE TABLE service_turns (
    `id` INTEGER NOT NULL AUTO_INCREMENT,
    `ticket_number` VARCHAR(30) NOT NULL,
    `customer_name` varchar(50),
    `created_by` varchar(50),
    `last_modified_by` varchar(50),
    `service_ending_expected` datetime,
    `service_started` datetime,
    `service_ended` datetime,
    `created` datetime NOT NULL,
    `last_modified` datetime NOT NULL,
    `status_id` INTEGER NOT NULL,
    `service_id` INTEGER NOT NULL,
    `priority_id` INTEGER NOT NULL,
    PRIMARY KEY (`id`),
    FOREIGN KEY(`status_id`) REFERENCES `statuses` (`id`),
    FOREIGN KEY(`service_id`) REFERENCES `services` (`id`),
    FOREIGN KEY(`priority_id`) REFERENCES `priorities` (`id`)
)

-- Base de dados Laboratórios de informática

-- Limpar a base de dados
DROP TABLE authors;
DROP TABLE comments;
DROP TABLE images;
DROP TABLE img_keys;
DROP TABLE keywords;

--Limpar dados das tabelas 

--TRUNCATE TABLE authors;
--TRUNCATE TABLE comments;
--TRUNCATE TABLE images;
--TRUNCATE TABLE img_keys;

-- Criar tabela 'IMAGES'
CREATE TABLE images (
	id				INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	id_image		TEXT NOT NULL,
	author_id		INTEGER NOT NULL,
	post_date		DATE NOT NULL,
	location		TEXT,
	votes_up		INTEGER,
	votes_down		INTEGER,
	secure			BOOLEAN NOT NULL,
	file_path		TEXT UNIQUE,
	views			INTEGER
);

-- Criar tabela 'COMMENTS'
CREATE TABLE comments (
	id			INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	post_date	DATE,
	author_id	INTEGER NOT NULL,
	message		TEXT NOT NULL,
	id_image	TEXT NOT NULL
);

-- Criar tabela 'AUTHORS'

CREATE TABLE authors (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	name	TEXT NOT NULL
);


-- Criar tabela 'KEYWORDS'

CREATE TABLE keywords (
	id	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	keyword	TEXT
);

-- Criar table 'IMG_KEYS'

CREATE TABLE img_keys (
	id_img		INTEGER NOT NULL,
	id_key 		INTEGER NOT NULL
);

CREATE DATABASE AQUARIO;

USE AQUARIO;

CREATE TABLE ALIMENTACAO(

	ID INT PRIMARY KEY AUTO_INCREMENT,
    ALIMENTADO BOOLEAN NOT NULL,
    DATA_ALIMENTACAO DATETIME

);

DROP TABLE ALIMENTACAO;

SELECT * FROM ALIMENTACAO;

INSERT INTO ALIMENTACAO(ALIMENTADO, DATA_ALIMENTACAO)
VALUES
(TRUE, sysdate());

INSERT INTO ALIMENTACAO(ALIMENTADO, DATA_ALIMENTACAO)
VALUES
(FALSE, sysdate());
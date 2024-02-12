create database cabeleleila_leila;

use cabeleleila_leila;

create table clientes (
	cadastro int not null auto_increment primary key,
    nome varchar (100) not null
);

create table servicos (
	horario datetime,
    servico varchar (30) not null,
    idservico int not null auto_increment primary key
);

select * from clientes ;
select * from servicos;
select * from agenda;

CREATE TABLE agenda (
	idagendamento int not null auto_increment,
    horarioescolhido DATETIME,
    idcadastro INT NOT NULL,
    idservico int not null,
    primary key (idagendamento),
    FOREIGN KEY (idservico) REFERENCES servicos(idservico),
    FOREIGN KEY (idcadastro) REFERENCES clientes(cadastro)
);

select c.cadastro, c.nome, s.servico, a.horarioescolhido, a.idcadastro, a.idagendamento from clientes c
join agenda a
on c.cadastro = a.idcadastro
join servicos s
on s.horario = a.horarioescolhido
order by a.horarioescolhido;

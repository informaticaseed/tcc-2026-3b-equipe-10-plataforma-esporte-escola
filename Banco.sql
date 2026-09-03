CREATE TABLE IF NOT EXISTS escolas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    endereco TEXT,
    telefone TEXT
);

CREATE TABLE IF NOT EXISTS esportes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS atividades (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    escola_id INTEGER NOT NULL,
    esporte_id INTEGER NOT NULL,
    dia_semana TEXT NOT NULL,
    horario TEXT NOT NULL,
    local TEXT,

    FOREIGN KEY (escola_id) REFERENCES escolas(id),
    FOREIGN KEY (esporte_id) REFERENCES esportes(id)
);

INSERT INTO esportes (nome, descricao) VALUES
('Futebol', 'Treinos e atividades de futebol'),
('Basquete', 'Treinos e atividades de basquete'),
('Vôlei', 'Treinos e atividades de voleibol'),
('Handebol', 'Treinos e atividades de handebol');

SELECT * FROM usuario

INSERT INTO usuario
(id, nome, senha, email, criado_em, atualizado_em)
VALUES
(1, 'Sophia Nader', 'sophia123', 'sophia@email.com', now(), NULL),
(2, 'Laura Silva', 'laura123', 'laura@email.com', now(), NULL),
(3, 'Gabriel Souza', 'gabriel123', 'gabriel@email.com', now(), NULL),
(4, 'Matheus Oliveira', 'matheus123', 'matheus@email.com', now(), NULL),
(5, 'Ana Beatriz', 'ana12345', 'ana@email.com', now(), NULL);

SELECT * FROM filmes

INSERT INTO filmes
(usuario_id, titulo, ano_lançamento, genero, nota, capa_url, criado_em, atualizado_em)
VALUES
(1, 'Interestelar', '2014-11-06', 'Ficção Científica', 9.5, 'https://exemplo.com/interestelar.jpg', now(), NULL),
(2, 'Vingadores: Ultimato', '2019-04-25', 'Ação', 9.0, 'https://exemplo.com/vingadores.jpg', now(), NULL),
(3, 'Homem-Aranha: Sem Volta para Casa', '2021-12-16', 'Ação', 8.5, 'https://exemplo.com/homemaranha.jpg', now(), NULL),
(4, 'Divertida Mente', '2015-06-18', 'Animação', 9.0, 'https://exemplo.com/divertidamente.jpg', now(), NULL),
(5, 'O Rei Leão', '1994-06-24', 'Animação', 9.5, 'https://exemplo.com/reileao.jpg', now(), NULL);


INSERT INTO usuario
(id, nome, senha, email, criado_em, atualizado_em)
VALUES
(1, 'Sophia Nader', 'sophia123', 'sophia@email.com', now(), NULL),
(2, 'Laura Silva', 'laura123', 'laura@email.com', now(), NULL),
(3, 'Gabriel Souza', 'gabriel123', 'gabriel@email.com', now(), NULL),
(4, 'Matheus Oliveira', 'matheus123', 'matheus@email.com', now(), NULL),
(5, 'Ana Beatriz', 'ana12345', 'ana@email.com', now(), NULL);



INSERT INTO filmes
(usuario_id, titulo, ano_lançamento, genero, nota, capa_url, criado_em, atualizado_em)
VALUES
(1, 'Interestelar', '2014-11-06', 'Ficção Científica', 9.5, 'https://i.pinimg.com/1200x/93/c4/c8/93c4c8ac622d2dd48846d53ece5b4183.jpg', now(), NULL),
(2, 'Vingadores: Ultimato', '2019-04-25', 'Ação', 9.0, 'https://i.pinimg.com/736x/cd/b3/b6/cdb3b63eb3ac1cf8faab32770c6dc3b5.jpg', now(), NULL),
(3, 'Homem-Aranha: Sem Volta para Casa', '2021-12-16', 'Ação', 8.5, 'https://i.pinimg.com/1200x/33/e5/a2/33e5a20674b21fd129b7dddfbf230a2d.jpg', now(), NULL),
(4, 'Divertida Mente', '2015-06-18', 'Animação', 9.0, 'https://i.pinimg.com/1200x/60/58/d2/6058d2e6027e1a6e68836119f93a3bb8.jpg', now(), NULL),
(5, 'O Rei Leão', '1994-06-24', 'Animação', 9.5, 'https://i.pinimg.com/736x/ee/73/35/ee733577a5724b59de70e4f1f335f874.jpg', now(), NULL);
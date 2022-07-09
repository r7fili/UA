--Selecionar todas as imagens pelas mais novas 
SELECT images.id_image, authors.name,images.votes_up,images.votes_down,images.views from images,authors where images.author_id = authors.id order by post_date DESC

--Selecionar todas as imagens pelas views
SELECT images.id_image, authors.name,images.votes_up,images.votes_down,images.views from images,authors where images.author_id = authors.id order by views DESC

--Comentários
    --Inserir comentário do que postou a foto
INSERT INTO comments (post_date, author_id, message, id_image) VALUES (datetime(),'{authorid[0][0]}','{desForm}','{imgname}')

--Selecionar uma imagem
SELECT images.id_image, authors.name,images.votes_up,images.votes_down, post_date,images.views from images,authors where images.author_id = authors.id and images.id_image LIKE '{body['id']}.%'

--Selecionar os comentários de uma dada imagem

SELECT comments.post_date, authors.name, comments.message from comments,authors WHERE comments.id_image = '' AND comments.author_id = authors.id--Selecionar todas as imagens pelas mais novas 
SELECT images.id_image, authors.name,images.votes_up,images.votes_down,images.views from images,authors where images.author_id = authors.id order by post_date DESC

--Selecionar todas as imagens pelas views
SELECT images.id_image, authors.name,images.votes_up,images.votes_down,images.views from images,authors where images.author_id = authors.id order by views DESC

--Comentários
    --Inserir comentário do que postou a foto
INSERT INTO comments (post_date, author_id, message, id_image) VALUES (datetime(),'{authorid[0][0]}','{desForm}','{imgname}')

--Selecionar uma imagem
SELECT images.id_image, authors.name,images.votes_up,images.votes_down, post_date,images.views from images,authors where images.author_id = authors.id and images.id_image LIKE '{body['id']}.%'

--Selecionar os comentários de uma dada imagem

SELECT comments.post_date, authors.name, comments.message from comments,authors WHERE comments.id_image = '' AND comments.author_id = authors.id
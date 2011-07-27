alter table posts_post add column tsv tsvector;

update posts_post set tsv = setweight(to_tsvector('english', coalesce(tags,'')), 'A') || setweight(to_tsvector('english', coalesce(title,'')), 'B') || setweight(to_tsvector('english', coalesce(body,'')), 'C');

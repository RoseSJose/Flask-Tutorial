drop table if exists registrants;

create table registrants(
    id serial primary key,
    name text not null,
    sport text not null
    );

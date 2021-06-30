drop table if exists shows;

create table shows(
    id serial primary key,
    title text not null
);

create table Car
(
    id      serial primary key,
    model   varchar(32),
    year    int,
    details text
);

insert into Car (model, "year", details)
values ('yaris', 2020, 'details'),
       ('golf 5', 2009, 'details'),
       ('astra', 2021, 'details');
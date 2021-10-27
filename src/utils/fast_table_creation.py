import mysql.connector

cnx = mysql.connector.connect(user='root', password='12345678',
                              host='127.0.0.1',
                              database='nasa')
tables = {}

## Create for eclss dust
data_id = 2
table_name = 'record%d'%data_id
tables[table_name] = ''.join(
    [
        "create table `%s` ("%table_name,
        "`synchronous_time` int unsigned NOT NULL,",
        "`time` int unsigned NOT NULL,",

    ] + [
        "`value%d` float,"%x for x in range(50)
        
    ] + [
        "primary key (`synchronous_time`), UNIQUE KEY `synchronous_time` (`synchronous_time`)",
        ")ENGINE=InnoDB"
        
    ]
)


## Create for eclss paint
data_id = 3
table_name = 'record%d'%data_id
tables[table_name] = ''.join(
    [
        "create table `%s` ("%table_name,
        "`synchronous_time` int unsigned NOT NULL,",
        "`time` int unsigned NOT NULL,",

    ] + [
        "`value%d` float,"%x for x in range(50)
        
    ] + [
        "primary key (`synchronous_time`), UNIQUE KEY `synchronous_time` (`synchronous_time`)",
        ")ENGINE=InnoDB"
        
    ]
)

## Create for npg dust
data_id = 4
table_name = 'record%d'%data_id
tables[table_name] = ''.join(
    [
        "create table `%s` ("%table_name,
        "`synchronous_time` int unsigned NOT NULL,",
        "`time` int unsigned NOT NULL,",

    ] + [
        "`value%d` float,"%x for x in range(1)
        
    ] + [
        "primary key (`synchronous_time`), UNIQUE KEY `synchronous_time` (`synchronous_time`)",
        ")ENGINE=InnoDB"
        
    ]
)


## Create for spg dust
data_id = 5
table_name = 'record%d'%data_id
tables[table_name] = ''.join(
    [
        "create table `%s` ("%table_name,
        "`synchronous_time` int unsigned NOT NULL,",
        "`time` int unsigned NOT NULL,",

    ] + [
        "`value%d` float,"%x for x in range(4)
        
    ] + [
        "primary key (`synchronous_time`), UNIQUE KEY `synchronous_time` (`synchronous_time`)",
        ")ENGINE=InnoDB"
        
    ]
)

## Create for spg dust
data_id = 6
table_name = 'record%d'%data_id
tables[table_name] = ''.join(
    [
        "create table `%s` ("%table_name,
        "`synchronous_time` int unsigned NOT NULL,",
        "`time` int unsigned NOT NULL,",

    ] + [
        "`value%d` float,"%x for x in range(1)
        
    ] + [
        "primary key (`synchronous_time`), UNIQUE KEY `synchronous_time` (`synchronous_time`)",
        ")ENGINE=InnoDB"
        
    ]
)

## Create for spg dust
data_id = 7
table_name = 'record%d'%data_id
tables[table_name] = ''.join(
    [
        "create table `%s` ("%table_name,
        "`synchronous_time` int unsigned NOT NULL,",
        "`time` int unsigned NOT NULL,",

    ] + [
        "`value%d` float,"%x for x in range(1)
        
    ] + [
        "primary key (`synchronous_time`), UNIQUE KEY `synchronous_time` (`synchronous_time`)",
        ")ENGINE=InnoDB"
        
    ]
)

cursor = cnx.cursor()

for key, value in tables.items():
    try:
        cursor.execute(value)
        print("Table %s has been created."%key)
    except:
        print("Table %s has already created."%key)
        
        
cnx.close()
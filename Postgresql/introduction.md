# Tutorial on Postgresql

## Author : Sudeshna Bora

---

### Step 1 : Installation in ubuntu

Follow [here](https://www.postgresql.org/download/linux/ubuntu/)

Post installing ```postgresql```, let us set it up .

```

ss -nlt

State                    Recv-Q                   Send-Q                                     Local Address:Port                                      Peer Address:Port                   Process                   
LISTEN                   0                        4096                                             0.0.0.0:111                                            0.0.0.0:*                                                
LISTEN                   0                        4096                                       127.0.0.53%lo:53                                             0.0.0.0:*                                                
LISTEN                   0                        5                                              127.0.0.1:631                                            0.0.0.0:*                                                
LISTEN                   0                        244                                            127.0.0.1:5432                                           0.0.0.0:* 
```

Should give a server running in port 5342.

## Step 2 : Setting up

### Step 2.1: Log into postgresql server

```
sudo -i -u postgres

#This changes the user to postgres 

```

### Step 2.2: Enter postgresql prompt

```
psql 
``` 

2.2.1) To exit postgresql prompt , type ```\q```.

### Step 2.3: Create user

Make sure you are ```postgres``` user.

```
createuser --interactive

```

### Step 2.4: Change user password

Log into postgresql and into the prompt


```
postgres=# \password postgres
Enter new password: <new-password>
postgres=# \q
```


### Step 2.5: To check users , be inside psql prompt and use ```\du```

```
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 admin     | Superuser, Create role, Create DB                          | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 subora    | Superuser, Create role, Create DB                          | {}

```

---


## Step 3: Data manipulation
 
### Step 3.1: Create database

The database created is same as the user 

```
createdb subora
```

<b>Note:</b> In case , the user (subora) is a sudo user , we can go into psql prompt directly by this following steps 

```
sudo -i -u subora 
psql 
```

In case , it is not . Add a new sudo user like 

```
sudo adduser admin
```

### Step 3.2: List all databases

Log into psql prompt.

```
postgres=# \l
                             List of databases
   Name    |  Owner   | Encoding | Collate | Ctype |   Access privileges   
-----------+----------+----------+---------+-------+-----------------------
 postgres  | postgres | UTF8     | en_IN   | en_IN | 
 subora    | postgres | UTF8     | en_IN   | en_IN | 
 template0 | postgres | UTF8     | en_IN   | en_IN | =c/postgres          +
           |          |          |         |       | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_IN   | en_IN | =c/postgres          +
           |          |          |         |       | postgres=CTc/postgres

```

### Step 3.3: Use particular database

Log into psql prompt

```
postgres=# \c <database_name>
You are now connected to database <database_name> as user "postgres".

```

### Step 3.4: List tables

Log into psql prompt

```
postgres=# \dt
         List of relations
 Schema |  Name  | Type  |  Owner   
--------+--------+-------+----------
 public | people | table | postgres
 public | posts  | table | postgres

```

### Step 3.5: check schema of a table

```
postgres=# \d <table_name>;
                                      Table "public.posts"
  Column   |           Type           | Collation | Nullable |              Default              
-----------+--------------------------+-----------+----------+-----------------------------------
 id        | integer                  |           | not null | nextval('posts_id_seq'::regclass)
 title     | character varying(255)   |           | not null | 
 content   | character varying(255)   |           | not null | 
 createdAt | timestamp with time zone |           | not null | 
 updatedAt | timestamp with time zone |           | not null | 
 personId  | integer                  |           |          | 
Indexes:
    "posts_pkey" PRIMARY KEY, btree (id)
Foreign-key constraints:
    "posts_personId_fkey" FOREIGN KEY ("personId") REFERENCES people(id) ON UPDATE CASCADE ON DELETE SET NULL

```
---
# Python Mysql Started

## 1. Create table 'Tasks' on your test database

```sql
CREATE TABLE `tasks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(80) NOT NULL,
  `description` text NOT NULL,
  `status` varchar(15) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
```

## 2. Create and set a .env file in root directory

```
DATABASE_HOST=localhost
DATABASE_USER=user
DATABASE_NAME=databasename
DATABASE_PASS=mypass
DATABASE_PORT=3306
```

## 3. Install requirements.txt

```
pip install -r requirements.txt
```

## 4. Run code

```
py script.py
```



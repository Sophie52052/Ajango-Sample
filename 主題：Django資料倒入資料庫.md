# 主題：Django資料倒入資料庫 講者：煌鑌, 怡瑄, 崇堯
###### tags: `Django` `Database` `DOS`
* cmd

Microsoft Windows [版本 10.0.14393]
(c) 2016 Microsoft Corporation. 著作權所有，並保留一切權利。


C:\Users\Sophie>cd C:\xampp\mysql\bin **(導向資料夾)**
```
cd C:\xampp\mysql\bin
```
C:\xampp\mysql\bin>mysql -u root **登入**
```
mysql -u root 登入
```
Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 11
Server version: 10.3.16-MariaDB mariadb.org binary distribution

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [(none)]> mysql -u root --default-character-set=utf8 <test> < kkbox_rs_2019-07-05_kkbox_song.sql **(mysql -u root代表在外面)**
    -> ;**(要加分號)(東西要放在bin不然要路徑)**

```
mysql -u root --default-character-set=utf8 <test> < kkbox_rs_2019-07-05_kkbox_song.sql ;
(mysql -u root代表在外面)(要加分號)(東西要放在bin不然要路徑)
```

ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'mysql -u root --default-character-set=utf8 <test> < kkbox_rs_2019-07-05_kkbox_so' at line 1

MariaDB [(none)]> create database hello;
```
create database hello;
```
Query OK, 1 row affected (0.007 sec)

MariaDB [(none)]> SHOW DATABASES;
```
SHOW DATABASES;
```

+--------------------+
| Database           |
+--------------------+
| hello              |
| information_schema |
| mysql              |
| performance_schema |
| phpmyadmin         |
| test               |
+--------------------+
6 rows in set (0.022 sec)

MariaDB [(none)]> SWITCH test
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'SWITCH test' at line 1
MariaDB [(none)]> use test;
```
use test;
```
**Database changed**
MariaDB [test]> mysql -u root --default-character-set=utf8 test < kkbox_rs_2019-07-05_kkbox_song.sql
    -> ;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'mysql -u root --default-character-set=utf8 test < kkbox_rs_2019-07-05_kkbox_song' at line 1
MariaDB [test]> 
**Ctrl-C -- exit!**

C:\xampp\mysql\bin>mysql -u root --default-character-set=utf8 test < kkbox_rs_2019-07-05_kkbox_song.sql **(倒入資料)(東西需在bin)**
```
mysql -u root --default-character-set=utf8 test < kkbox_rs_2019-07-05_kkbox_song.sql
```
C:\xampp\mysql\bin>mysql -u root --default-character-set=utf8 test < kkbox_rs_2019-07-05_userlike_record.sql
```
mysql -u root --default-character-set=utf8 test < kkbox_rs_2019-07-05_userlike_record.sql
```

> https://drive.google.com/drive/u/1/folders/17gWrSbHey1_M4r05u7xw-Wj8afoNDS4W

> https://charlychiu.github.io/presentation/NCKU-CSIE-IIR-Summer-Course/index.html#/

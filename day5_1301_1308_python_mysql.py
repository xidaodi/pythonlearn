import pymysql.cursors

# 连接到数据库

connections=pymysql.connect(host="localhost",
                            port=3306,
                            user="root",
                            password="esaye=mc2909",
                            db="world",
                            charset="utf8",
                            cursorclass=pymysql.cursors.DictCursor)


try:
    with connections.cursor() as cursor:

        #查看全部数据库
        sql="show databases"
        dbs=cursor.execute(sql)
        result=cursor.fetchall()
        print(dbs)
        print(result)
        connections.commit()

    with connections.cursor() as cursor:

        #创建表
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
        sql="""CREATE TABLE EMPLOYEE(
                FIRST_NAME  CHAR(20)  NOT NULL,
                LAST_NAME   CHAR(20),
                AGE INT,
                SEX CHAR(1),
                INCOME FLOAT)
        """
        dbs=cursor.execute(sql)
        connections.commit()
        sql="show tables"
        dbs=cursor.execute(sql)
        result=cursor.fetchall()
        print(dbs)
        print(result)

    with connections.cursor() as cursor:
        #插入数据

        sql="""INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
               VALUES("RJ","C",20,"F",2000)
        """
        try:
            nrow=cursor.execute(sql)  # nrow 代表影响的行数

            print(nrow)
            connections.commit()
        except:
            connections.rollback()

    with connections.cursor() as cursor:
        #查询数据

        sql="select * from city"

        try:
            data=cursor.execute(sql)
            print(data)
            result=cursor.fetchall()
            for row in result:
                id=row["ID"]
                name=row["Name"]
                CountryCode=row["CountryCode"]
                print(id,name,CountryCode)


        except:
            print("数据查询失败")

    with connections.cursor() as cursor:

        #数据更新
        sql="UPDATE EMPLOYEE SET AGE=30 WHERE LAST_NAME='c'"

        try:
            row=cursor.execute(sql)
            connections.commit()
        except:
            connections.rollback()

    with connections.cursor() as cursor:

        #数据删除
        sql="DELETE FROM EMPLOYEE WHERE LAST_NAME='c'"

        try:
            row=cursor.execute(sql)
            connections.commit()
        except:
            connections.rollback()


finally:
    connections.close()
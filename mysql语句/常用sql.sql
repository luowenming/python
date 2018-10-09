--库 操作

--显示当前所有库名
--show databases;

--创建库 python是库名
--CREATE database python charset=utf8;

--删除库 
--drop database python;

--查看当前使用的库
--select database();

--使用某个库
--use python


--表 操作

--查看当前库下面所有的表
--show tables;

--创建一张表
-- demo是表名
-- unsigned 无符号
-- not null 不能为空
-- auto_increment 是自动增长
-- PRIMARY KEY 设置主键
-- CREATE table students(
--     id int unsigned not null auto_increment PRIMARY KEY,
--     name VARCHAR(30) default '',
--     age TINYINT unsigned default 0,
--     high DECIMAL(5,2),
--     gender enum("男", "女", "中性", "保密") default "保密",
--     cls_id int unsigned,
--     is_delete bit default 0
-- );

-- CREATE table classess(
--     id int unsigned not null auto_increment PRIMARY KEY,
--     name VARCHAR(30)
-- );

--查看表结构
--desc demo;

--修改表-添加字段
--ALTER table demo add birthday datetime;

--修改表-修改字段：不重命名版
--ALTER table demo MODIFY birthday date;

--修改表-修改字段：重命名版
--ALTER TABLE demo change birthday birth date;

--修改表-删除字段
--ALTER TABLE demo drop hige

--删除表
--drop table demo


--增删改查(curd)
  --增加
    --全列插入
    --INSERT INTO classess VALUES(0, "大神班");

    --部分插入
    --INSERT INTO classess (name, gender) VALUES("小乔", 2);

    --多行插入
    --INSERT INTO classess (name, gender) VALUES("大敲", 1),("貂蝉", 3)

--修改
    -- UPDATE classess set age=1,gender=2; --全部都改
    -- UPDATE classess set age=1,gender=2 where name="张三"; --只要name=张三的全部修改
    -- UPDATE classess set age=1,gender=2 where id=3; --只要id为3的，进修改

--查询
    --select * from classess; --全部查询

    --指定查询条件
    --select * from classess where name="小乔"; --查询name等于小乔

    --查询指定列
    --select name,gender from classess;

--删除数据
    --delete FROM classess; --删除整个表所有数据



--准备数据
-- INSERT INTO students VALUES
-- (0,"小明",18,180.00,2,1,0),
-- (0,"小月月",18,180.00,2,2,1),
-- (0,"彭于晏",25,185.00,1,1,0),
-- (0,"刘德华",59,175.00,1,2,1),
-- (0,"黄蓉",38,160.00,2,1,0),
-- (0,"凤姐",28,150.00,4,1,1),
-- (0,"王祖贤",18,172.00,2,1,1),
-- (0,"周杰伦",36,172.00,2,1,0),
-- (0,"程坤",27,181.00,1,2,0),
-- (0,"刘亦菲",25,166.00,2,2,0),
-- (0,"金星",33,162.00,2,2,1),
-- (0,"静香",12,170.00,2,4,0),
-- (0,"郭靖",12,170.00,1,4,0),
-- (0,"周杰",36,172.00,2,5,0)


--给表取别名
--select s.name,s.age from students as s;


--条件查询
    --比较运算符
        -- > < = !=或者<> >= <=
        --查询大于18岁
        select * from students where age>18;

        --查询小于18岁
        select * from students where age<18;

        --查询等于18岁
        select * from students where age=18;
    
    --逻辑运算符
        -- and
        --18到28之间的所有学生信息
        select * from students where age>18 and age<28;

        --18岁以上的女性
        select * from students where age>18 and gender="女";

        --or
        --18以上或者身高超过180(包含)以上
        select * from students where age>18 or high>=180;

        --not
        --不在18岁以上的女性
        select * from students where not (age>18 and gender="女");

        --年龄不是小于或者等于18 并且是女性
        select * from students where not age<=18 and gender="女";
    
    --模糊查询
        -- like
        -- %替换1个或者多个
        -- _替换1个

        -- 查询姓名中 以“小”开始的名字
        select name from students where name like "小%";

        -- 查询姓名中 有“小”的名字
        select name from students where name like "%小%";

        --查询有2个字的名字
        select * from students where name like "__";

        --查询有3个字的名字
        select * from students where name like "___";

        --查询有两个（包含）以上的名字
        select * from students where name like "__%";

        -- rlike 正则
        --查询以 周开始的姓名
        select * from students where name rlike "^周.*";

        --查询以 周开始 以伦结尾的姓名
        select * from students where name rlike "^周.*伦$";

    --范围查询
        --in (1, 3, 8)表示在一个非连续的范围内
        --查询 年龄为18、24、34的姓名
        select * from students where age in (12,18,38,59);

        --not in 不非连续的范围之内
        --查询年龄不是18，34岁的信息
        select * from students where age not in (18,34);
        
        --between ... and ... 表示在一个连续的范围内
        --查询 年龄在18-34之间的信息
        select * from students where age between 18 and 34;

        -- not between ... and ...
        --查询不在18到34之间的信息
        select * from students where age not between 18 and 34;

    --排序
        --order by
        -- asc从小到大排序，升序
        -- desc从大到小排序，降序

        --查询年龄在18到34岁之间的男性，按照年龄从小到大排序
        select * from students where (age between 18 and 34) and gender="男" order by age;

        --查询年龄在18到34岁之间的女性，身高从高到矮排序
        select * from students where (age between 12 and 50) and gender="女" order by high desc;

        --order by 多个字段
        --查询年龄在18到34岁之间的女性，身高从高到矮排序，如果身高想同的情况下按照年龄从小到大排序
        select * from students where (age between 18 and 34) and gender="女" order by high desc,id desc;

        --按照年龄从小到大排序，身高从高到矮排序
        select * from students order by age asc,high desc;

    --聚合函数
        --总数
        -- count
        --查询男性有多少人，女性有多少人
        select count(*) from students where gender=1;
        select count(*) as 女性人数 from students where gender=2;

        -- 最大值
        -- max
        -- 查询最大的年龄
        select max(age) from students;

        --查询女性最高的身高
        select max(high) from students where gender=2;


        --最小值
        --min

        --求和
        --sum

        --平均值
        --avg

        --四舍五入 round
        --计算所有人的平均年龄，保留2位小
        select round(avg(age),2) from students;



















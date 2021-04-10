--DROP TABLE emp PURGE;

-- CREATE TABLE emp (
--   empno    NUMBER(4) CONSTRAINT pk_emp PRIMARY KEY,
--   ename    VARCHAR2(10),
--   job      VARCHAR2(9),
--   mgr      NUMBER(4),
--   hiredate DATE,
--   sal      NUMBER(7,2),
--   comm     NUMBER(7,2),
--   deptno   NUMBER(2)
-- );

select deptno,
-- listagg(ename, ', ') within group (order by ename desc) as agg_str
-- first_value(sal) ignore nulls over(partition by deptno order by deptno, sal) as f_v
-- sum(sal) over(partition by deptno order by deptno, sal range between unbounded preceding and current row ) range_between,
-- sum(sal) over(partition by deptno order by deptno, sal rows between unbounded preceding and current row) rows_between
from emp e;

select empno,ename,sys_connect_by_path(ename,'/'),mgr, prior ename
from emp
connect by prior empno = mgr
start with mgr is null;

select substr('sapan',level,1) from dual
connect by level <= length('sapan');


select mgr, count(empno),
rank() over(order by count(empno)) as t_sum
from emp
group by mgr;

select mgr, listagg(ename,', ') within group (order by ename) as emps
from emp
group by mgr;

select to_date('2019-09-12 23:12:45','YYYY-MM-DD HH24:MI:SS') from dual;
select to_char(sysdate,'YYYY-MM-DD HH24:MI:SS') from dual;
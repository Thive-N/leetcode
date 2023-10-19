select max(st.num) as num
from ( select t.num 
       from MyNumbers t 
       group by t.num 
       having count(t.num) = 1 
     ) as st;
-- Use the `ref` function to select from other models

select *
from "ashbabotanics"."dbt_kcx"."my_first_dbt_model"
where id = 1
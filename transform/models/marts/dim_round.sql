with rounds as (
    
    select * from {{ref('stg_sportsapi365__matches')}}
)

select distinct round_id  as round_id, -- jag hämtar alla unika rund_id från matches

from rounds

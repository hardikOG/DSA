# Write your MySQL query statement below
SELECT
    date_format(trans_date, '%Y-%m') as month,
    country,
    count(*) as trans_count,
    sum(state = 'approved') as approved_count,
    sum(amount) as trans_total_amount,
    sum(CASE when state = 'approved' then amount else 0 END) as approved_total_amount
FROM transactions
GROUP by date_format(trans_date, '%Y-%m'), country
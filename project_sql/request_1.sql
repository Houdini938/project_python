SELECT 
    t.date AS date,
    SUM(t.prod_price * t.prod_qty) AS ventes
FROM 
    TRANSACTION t
JOIN 
    PRODUCT_NOMENCLATURE p ON t.prop_id = p.product_id
WHERE 
    t.date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY 
    t.date
ORDER BY 
    t.date;

LESSONS_BY_STUDENT = """
SELECT
    st.first_name,
    st.last_name,
    sub.subject_name,
    COUNT(*) AS lessons_count,
    SUM(lst.final_cost) AS total_sum
FROM lessons_student_total_info lst
LEFT JOIN students st ON st.student_id = lst.student_id
LEFT JOIN subjects sub ON sub.subject_id = lst.subject_id
WHERE
    (%(student_id)s IS NULL OR lst.student_id = %(student_id)s)
    AND (%(date_from)s IS NULL OR lst.date >= %(date_from)s)
    AND (%(date_to)s IS NULL OR lst.date <= %(date_to)s)
GROUP BY st.first_name, st.last_name, sub.subject_name

UNION ALL

SELECT
    NULL::varchar,
    NULL::varchar,
    'TOTAL',
    NULL::bigint,
    SUM(lst.final_cost)
FROM lessons_student_total_info lst
WHERE
    (%(student_id)s IS NULL OR lst.student_id = %(student_id)s)
    AND (%(date_from)s IS NULL OR lst.date >= %(date_from)s)
    AND (%(date_to)s IS NULL OR lst.date <= %(date_to)s);
"""


STUDENT_BALANCES = """
SELECT
    st.student_id,
    st.first_name,
    st.last_name,
    SUM(lst.final_cost) AS total_for_lessons,
    COALESCE(pay.amount_paid, 0) AS amount_paid,
    COALESCE(pay.amount_paid, 0) - SUM(lst.final_cost) AS balance
FROM lessons_student_total_info lst
LEFT JOIN students st ON st.student_id = lst.student_id
LEFT JOIN (
    SELECT student_id, SUM(amount) AS amount_paid
    FROM payments
    WHERE
        (%(date_from)s IS NULL OR date >= %(date_from)s)
        AND (%(date_to)s IS NULL OR date <= %(date_to)s)
    GROUP BY student_id
) pay ON st.student_id = pay.student_id
WHERE
    (%(date_from)s IS NULL OR lst.date >= %(date_from)s)
    AND (%(date_to)s IS NULL OR lst.date <= %(date_to)s)
GROUP BY st.student_id, st.first_name, st.last_name, pay.amount_paid
ORDER BY total_for_lessons DESC;
"""


PAYMENTS_AGGREGATED = """
SELECT
    st.student_id,
    st.first_name,
    st.last_name,
    SUM(p.amount) AS amount_paid
FROM payments p
LEFT JOIN students st ON st.student_id = p.student_id
WHERE
    (%(date_from)s IS NULL OR p.date >= %(date_from)s)
    AND (%(date_to)s IS NULL OR p.date <= %(date_to)s)
GROUP BY st.student_id, st.first_name, st.last_name;
"""

PAYMENTS_TOTAL = """
SELECT
    st.student_id,
    st.first_name,
    st.last_name,
    SUM(p.amount)::bigint AS amount_paid
FROM payments p
JOIN students st ON st.student_id = p.student_id
WHERE
    (%(date_from)s IS NULL OR p.date >= %(date_from)s)
    AND (%(date_to)s IS NULL OR p.date <= %(date_to)s)
GROUP BY st.student_id, st.first_name, st.last_name
ORDER BY amount_paid DESC;
"""

select_all_female_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE sex = 'F';
"""

select_alive_brown_bears_return_name_and_age = """
    SELECT
        name,
        age
    FROM bears
    WHERE alive = 1 AND color = 'Brown';
"""

select_youngest_bear_return_name = """
    SELECT
        name
    FROM bears
    WHERE age = (SELECT MIN(age) FROM bears);
"""

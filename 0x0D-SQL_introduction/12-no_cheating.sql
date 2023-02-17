-- updates bobs score without using id value
UPDATE second_table as s
SET s.score = 10
WHERE s.name = "Bob";
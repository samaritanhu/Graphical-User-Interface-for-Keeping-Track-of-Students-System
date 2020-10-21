# 1.allow new students to enroll into the program
INSERT_STU = """
INSERT INTO students
VALUES
(DEFAULT, '%s', %d);
"""

# 2.new courses to be introduced
# KNOWN course_id
INSERT_COURSE = """
INSERT INTO courses
VALUES
(DEFAULT, %d, '%s', '%s', %d);
"""

# 3.students to enroll in courses
INSERT_STU_COURSE = """
INSERT INTO student_course
VALUES
(%d, %d);
"""

# 4. querying to see which students are in each course

# 4.1. KNOWN course_id
SEARCH_STU1 = """
SELECT 
s.student_id, student_name
FROM 
student_course sc 
JOIN students s 
ON sc.student_id = s.student_id 
WHERE sc.course_id = %d;
"""

# 4.2. KNOWN course_name
SEARCH_STU2 = """
SELECT 
s.student_id, student_name
FROM 
student_course sc 
JOIN students s 
ON sc.student_id = s.student_id 
WHERE sc.course_name = '%s';
"""

# 5.querying to see which courses each student is in
# 5.1. KNOWN student_id
SEARCH_COURSE1 = """
SELECT 
course_name, course_time, course_week
FROM 
student_course sc 
JOIN courses c
ON sc.course_id = c.course_id 
WHERE sc.student_id = %d;
"""

# 5.2. KNOWN student_name
SEARCH_COURSE2 = """
SELECT 
course_name, course_time, course_week
FROM 
student_course sc 
JOIN courses c
ON sc.course_id = c.course_id 
JOIN students s 
ON sc.student_id = s.student_id 
WHERE s.student_name = '%s';
"""

# 6.querying to see which courses and what times each course is for a given student on a given day of the week.
SEARCH_STU_COURSE = """
SELECT sc.course_id, course_name, course_time
FROM
student_course sc 
JOIN courses c
ON sc.course_id = c.course_id 
JOIN students s 
ON sc.student_id = s.student_id 
WHERE s.student_id = %d
AND c.course_week = %d 
"""
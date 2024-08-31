from src.courses import Course, CourseList
from datetime import datetime


season = "fall"
now = datetime.now()
term = ''

if season.lower() == 'spring':
    term = f'{now.year + 1}' + '02' if now.month > 4 else f'{now.year}' + '02'
else:
    term = f'{now.year}' + '05' if season.lower() == 'summer' else f'{now.year}' + '08'

# Sci Foundation of Health - 88239 - APPH 1040 - G
# Data Struct & Algorithms - 81688 - CS 1332 - A
# Data Struct & Algorithms - 83879 - CS 1332 - B
# Objects and Design - 90395 - CS 2340 - C
# Objects and Design - 92136 - CS 2340 - D
# Sci Foundation of Health - 84066 - APPH 1040 - A
# Sci Foundation of Health - 83639 - APPH 1040 - J
# Sci Foundation of Health - 85435 - APPH 1040 - B
# Sci Foundation of Health - 88605 - APPH 1040 - C
# Sci Foundation of Health - 83638 - APPH 1040 - E
# Sensation & Perception - 83587 - PSYC 3040 - A
# Computer Organiz&Program - 82498 - CS 2110 - A
# Computer Organiz&Program - 86990 - CS 2110 - A01
# Computer Organiz&Program - 86991 - CS 2110 - A02
# Computer Organiz&Program - 86992 - CS 2110 - A03
# Computer Organiz&Program - 87147 - CS 2110 - C
# Computer Organiz&Program - 87148 - CS 2110 - C01
# Computer Organiz&Program - 87150 - CS 2110 - C02
# Computer Organiz&Program - 91387 - CS 2110 - C04
# Computer Organiz&Program - 91388 - CS 2110 - C05
# Intro Discrete Math CS - 89225 - CS 2050 - C
# Intro Discrete Math CS - 82928 - CS 2050 - A

crns = ['86991', '86992', '82928', '88421']
courses = [Course(crn, term) for crn in crns]
print("\n\n")
lst = CourseList(courses)
lst.run_notifier_email()

class TeachingData:
    def __init__(self, course_code, course_name, instructor, department, semester, year, enrollment_count):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor = instructor
        self.department = department
        self.semester = semester
        self.year = year
        self.enrollment_count = enrollment_count

    @classmethod
    def from_dict(cls, data):
        return cls(
            course_code=data.get('course_code'),
            course_name=data.get('course_name'),
            instructor=data.get('instructor'),
            department=data.get('department'),
            semester=data.get('semester'),
            year=data.get('year'),
            enrollment_count=data.get('enrollment_count')
        )

    def to_dict(self):
        return {
            'course_code': self.course_code,
            'course_name': self.course_name,
            'instructor': self.instructor,
            'department': self.department,
            'semester': self.semester,
            'year': self.year,
            'enrollment_count': self.enrollment_count
        }
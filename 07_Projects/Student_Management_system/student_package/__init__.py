# student_package/__init__.py
from .student_utils import (
    add_students,
    view_all_students,
    sort_students,
    search_student,
    del_student,
    print_students,
    get_valid_input,
    generate_student_id,
    export_students,
    validate_name,
    validate_age,
    validate_courses,
    validate_gpa,
    import_students,
    binary_search_by_id
)

from .student import Student
from .database import save_students, load_students, add_student

__all__ = [
    "add_students",
    "view_all_students",
    "sort_students",
    "search_student",
    "binary_search_by_id",
    "del_student",
    "print_students",
    "get_valid_input",
    "generate_student_id",
    "export_students",
    "validate_name",
    "validate_age",
    "validate_courses",
    "validate_gpa",
    "Student",
    "save_students",
    "load_students",
    "add_student",
    "import_students"
]

__version__ = "1.0.0"
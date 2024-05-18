from .student import student_bp
from .instructor import instructor_bp
from .program import program_bp
from .license import license_bp
from .aiu import aiu_bp
from .coursera import coursera_bp
from .home import home_bp
from .coordinator import coordinator_bp

__all__ = [
    'home_bp',
    'student_bp',
    'instructor_bp',
    'program_bp',
    'license_bp',
    'aiu_bp',
    'coursera_bp',
    'coordinator_bp'
]

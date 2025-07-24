# Force import resolution
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from .birth_chart_calculator import calculate_birth_chart
__all__ = ['calculate_birth_chart']
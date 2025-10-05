import sys
sys.path.insert(0, '../src')
import cleaning

def test_restaurant_cleaning():
    """Test restaurant cleaning function."""
    cleaning.restaurant_cleaning()

def test_restroom_cleaning():
    """Test restroom cleaning function."""
    cleaning.restroom_cleaning()

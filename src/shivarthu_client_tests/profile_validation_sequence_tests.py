import unittest
from test_class.profile_validation import ProfileValidationTests

# Load the test case class
class_name = ProfileValidationTests

# Create a test loader
loader = unittest.TestLoader()

# Load the test methods in the desired order
class_methods = [
    class_name('test_add_profile'),
    class_name('test_add_profile_stake'),    
]

# Create a test suite
test_suite = unittest.TestSuite(class_methods)

runner = unittest.TextTestRunner()


# Run the test suite
runner.run(test_suite)
import unittest
from tests.AccountLogin import AccountLogin
from tests.RegistrationForm import RegistrationForm


# Pobierz testy, które chcesz uruchomić
test_1 = unittest.TestLoader().loadTestsFromTestCase(AccountLogin)
test_2 = unittest.TestLoader().loadTestsFromTestCase(RegistrationForm)

# Stwórz Test Suita łączac testy
test_suite = unittest.TestSuite([test_1])
test_suite = unittest.TestSuite([test_2])

# odpal
unittest.TextTestRunner(verbosity=2).run(test_suite)
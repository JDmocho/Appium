import unittest
from tests.AccountLogin import AccountLogin

# Pobierz testy, które chcesz uruchomić
test_1 = unittest.TestLoader().loadTestsFromTestCase(AccountLogin)


# Stwórz Test Suita łączac testy
test_suite = unittest.TestSuite([test_1])

# odpal
unittest.TextTestRunner(verbosity=2).run(test_suite)
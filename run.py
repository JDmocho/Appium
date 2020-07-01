import unittest
from tests.AccountLogin import AccountLogin
from tests.RegistrationForm import RegistrationForm
from tests.ShopDouglas import ShopDouglas



# Pobierz testy, które chcesz uruchomić
#test_1 = unittest.TestLoader().loadTestsFromTestCase(AccountLogin)
#test_2 = unittest.TestLoader().loadTestsFromTestCase(RegistrationForm)
test_3 = unittest.TestLoader().loadTestsFromTestCase(ShopDouglas)

# Stwórz Test Suita łączac testy
test_suite = unittest.TestSuite([test_3])


# odpal
unittest.TextTestRunner(verbosity=2).run(test_suite)
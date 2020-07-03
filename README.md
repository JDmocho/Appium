# Appium

### Features

Automation of test cases for the Android mobile application with Appium. In this example we will test the mobile application: Douglas

### Environment

- java: 1.8.0_252
- Android Studio: 4.0
- node.js: 14.4.0
- npm: 6.14.5
- appium: V1.15.1
- appium-doctor: v.1.15.3
- Pycharm: 2020.1.2
- Python: 3.6.9
- pip: 20.1.1
- Appium Python Client: 1.0.1
- selenium: 3.141.0

### Before you start:

Before you run tests, be sure to prepare environment. After that you need to connect do device. If you want connect to Android with adb over TCP, connect your phone by USB cable and run:

`adb tcpip 5555`

Remember to set  ANROID_SDK_PATH  and  DEVICE_IP (phone IP) in Makefile 
After that you should be able to connect your phone over WiFi.

To connect:

`make connect`

Check if device is connected:

`make status`

Sometimes you need to disconnect and connect again, because _make status_ return that device is offline:

`make disconnect`

`make connect`

If _make status_ still return offline status, just turnoff WiFi and try turn on again. 
_make connect_ and check status.

To run Appium:

`make appium`

To run uiautomatorviewer:

`make viewer`


### Run tests:

You can run tests traditional 

`python run.py`

or run application more efficiently with makefile. The make utility requires a file, Makefile (or makefile), which defines set of tasks to be executed.

`make tests`

If you don’t want run all tests, but only specific test, modify  test suit in run.py
For example, run only first and second test:

    test_1 = unittest.TestLoader().loadTestsFromTestCase(AccountLogin)
    test_2 = unittest.TestLoader().loadTestsFromTestCase(RegistrationForm)
    test_3 = unittest.TestLoader().loadTestsFromTestCase(ShopDouglas)

    test_suite = unittest.TestSuite([test_1, test_2])

### The folder structure:

    ├── data
    │   ├── bad_email_account.csv
    │   ├── bad_password_account.csv
    │   ├── incorrect_email_registration.csv
    │   └── incorrect_password_registration.csv
    ├── library
    │   └── GetData.py
    ├── tests
    │   ├── AccountLogin.py
    │   ├── RegistrationForm.py
    │   └── ShopDouglas.py
    ├── .gitignore
    ├── DouglasParfumKosmetik_v7.8.4_apkpure.com.apk
    ├── Makefile
    ├── README.md
    ├── requirements.txt
    └── run.py
    

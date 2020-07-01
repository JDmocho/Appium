ANROID_SDK_PATH=/home/joanna/Android/Sdk/tools/bin/
DEVICE_IP=192.168.1.12:5555

connect:
	adb connect $(DEVICE_IP)

disconnect:
	adb disconnect $(DEVICE_IP)

status:
	adb devices

appium:
	appium

viewer:
	cd $(ANROID_SDK_PATH) && ./uiautomatorviewer

test:
	python run.py


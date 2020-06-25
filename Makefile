ANROID_SDK_PATH=/home/joanna/Android/Sdk/tools/bin/
DEVICE_IP=192.168.1.12:5555

prepare:
	adb connect $(DEVICE_IP)
	appium

viewer:
	cd $(ANROID_SDK_PATH) && ./uiautomatorviewer

test:
	python run.py




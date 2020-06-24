ANROID_SDK_PATH=/home/joanna/Android/sdk/tools/bin/
DEVICE_IP=192.168.1.12:5555

prepare:
	appium
	cd $(ANROID_SDK_PATH)
	./uiautomatorviewer
	adb connect $(DEVICE_IP)

test:
	python run.py




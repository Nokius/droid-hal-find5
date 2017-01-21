# These and other macros are documented in dhd/droid-hal-device.inc
%define device find5
%define vendor oppo

%define vendor_pretty OPPO
%define device_pretty Find5

%define installable_zip 1

%define straggler_files \
/at.rle\
/fastboot.rle\
/initlogo.rle\
/tpupdate.rle\
/wlan.rle\
%{nil} 

#For OTA
%define enable_kernel_update 1

%include rpm/dhd/droid-hal-device.inc

[app]
title = Sentinel
package.name = sentinel
package.domain = org.sentinel
source.dir =.
source.include_exts = py,png,jpg,json,txt
version = 1.0
requirements = python3,kivy==2.3.0,opencv==4.9.0.80,Pillow,numpy
orientation = portrait
fullscreen = 0

[buildozer]
log_level = 2

[app:requirements]
android.permissions = CAMERA,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[app:android]
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license_agreement = True

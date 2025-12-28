[app]
title = Jarvis Remote
package.name = jarvisremote
package.domain = org.soulcommander
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
# FULL REQUIREMENTS (Video + Audio + Internet)
requirements = python3,kivy,requests,plyer,urllib3,certifi,idna,charset_normalizer,ffmpeg,ffpyplayer
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,MANAGE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1

@echo off

rmdir /s /q build
rmdir /s /q dist
del /q esp32_base_station.spec

pyinstaller --onefile ^
--noconsole ^
--name esp32_base_station ^
--add-data "handlers\resources\doorbell.wav;handlers\resources" ^
--hidden-import handlers.doorbell ^
--hidden-import handlers.spotify ^
esp32_base_station.py

copy handlers\.env dist\.env

pause
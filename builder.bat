@echo off

rmdir /s /q build
rmdir /s /q dist
del /q listener.spec

pyinstaller --onefile ^
--noconsole ^
--name esp32_base_station ^
--add-data "handlers\resources\doorbell.wav;handlers\resources" ^
--hidden-import handlers.doorbell ^
esp32_base_station.py

pause
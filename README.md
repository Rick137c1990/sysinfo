# Sysinfo

Проект представляет собой небольшую системную утилиту, написанную на языке Python.

Утилита `sysinfo` предназначена для быстрого получения информации о локальном компьютере или сервере.

## Возможности

Утилита позволяет получить следующую информацию:

1. **Операционная система**

   Примеры:
   - Linux
   - Darwin (macOS)

2. **Имя хоста**

   Пример:
   - MacBook-Air.local

3. **Версия ядра операционной системы**

4. **Архитектура системы**

   Пример:
   - 64bit

5. **Версия Python**

6. **IP-адрес устройства**

7. **Информация о процессоре (CPU)**

   Пример:
   - ARM

8. **Оперативная память (RAM)**

   Отображается:
   - общий объём памяти;
   - доступная память;
   - используемая память;
   - свободная память;
   - процент загрузки.

---

## Пример работы

```text
=============== System ===============
OS             : Darwin
Hostname       : Sergej--MacBook-Air.local
Kernel         : 25.5.0
Architecture   : 64bit

=============== Python ===============
Version        : 3.11.7

=============== Network ===============
IP             : 192.168.1.109

=============== CPU ===============
CPU            : arm

=============== RAM ===============
Total          : 8.00 GB
Available      : 1.61 GB
Used           : 2.92 GB
Free           : 0.07 GB
Percent        : 79.9%
```
## Установка
Клонировать репозиторий:  
```bash
git clone <repository-url>
```
Перейти в директорию проекта:  
```bash
cd sysinfo
```
Создать виртуальное окружение:  
```bash
python -m venv .venv
```
Активировать виртуальное окружение:
Linux / macOS  
```bash
source .venv/bin/activate
```
Windows  
```bash
.venv\Scripts\activate
```
Установить зависимости:  
```bash
pip install -e .
```
### Требования  
Версия Python: >= 3.11

Структура проекта:
```bash
sysinfo/  
│  
├── src/  
│   ├── main.py  
│   └── sysinfo.py  
│  
├── README.md  
├── pyproject.toml  
├── .python-version  
└── .gitignore  
```
Используемые технологии:  
```bash
Python 3  
psutil  
socket  
platform  
Git
```
Автор: Sergej Nazarov
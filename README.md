# RaspiApp

## License
The MIT License (MIT)

Copyright (c) 2015 Rafael Sillero

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Instalation
### Server side (Raspberry Pi)
Copy the 'server' folder into your Raspberry Pi.
Install nodejs and npm.
Use 'npm install' inside 'server' folder.
Use 'node app.js' inside 'server' folder.
Wait for an OK message.

### Client side (Ubuntu)
Copy the 'client' folder into your Ubuntu PC.
Install python if you still haven't got it.
Edit 'main.py' and set 'ip_of_raspberry_pi' to whatever you Raspi's IP is.
Give execute permissions to both 'RaspiApp' and 'main.py'.

## Usage
You can launch it in three different ways:
- python main.py
- ./main.py
- ./RaspApp

Only the last one brings you back a free console.
To check the Raspberry temperature, just click on the icon and select 'Temperatura'.

Click 'Salir' to close the tray icon.

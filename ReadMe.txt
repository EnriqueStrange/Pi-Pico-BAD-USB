FOR EDUCATIONAL PURPOSES ONLY...

So we installed rp2-pico file to make it programeable and then we installed adafruit circuitpython to make it a keyboard and mouse emulator.
and then we created a program that runs cmd using win + R shortcut and then it makes a curl request to download the backdoor file and then runs it by just filename.exe
we are using https://app.mediafire.com as a storage to make a download link for the backdoor(Google drive is not taken in option because it asks for verification which may not be bypassed without any additional softaware)
In the part of advanced backdoor we were making socket connection using the local ip but this time we wanted it to be in public network ip so I used ngrok(reffer https://ngrok.com for more information)(by port forwarding) to run the server for reverse connection in public ip.
We got a problem that the advanced backdoor when converted to exe it goes to a size of 60 mb even when compressed so we are using another option that we are creating a basic backdoor that just is able to run cmd and make persistent(Make the backdoor autorun run after reboot) to reduce the exe size to make it download faster and also run faster because we dont want out victims to know that we are trying to get remote access to their computer.Then we are going to run curl and install the advanced backdoor remotely.

FOR MORE REFFER TO OUR YOUTBE CHANNEL - STRANGE LEARNINGS(https://youtu.be/NZASumkG6M8)

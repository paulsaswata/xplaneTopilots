# Xplane 9 Data.txt to PILOTS TCP transfer module 

#### This python code can be used to transfer data from Xplane Data.txt to  a [PILOTS program](https://github.com/RPI-WCL/pilots/)

* The `xplaneDataToPilotsTcp.py` code provided here can be modified easily to transfer data from Xplane's Data.txt file to a PILOT program's TCP socket. 

* The code, in its vanilla state, transfers the `alpha,__deg` and `Vtrue,_ktas` as `aoa` and `v` respectively to the PILOTS program server.

* The code can also be used to interactively inject errors in the transferred data.

##### Instructions for modifying the code:
###### Changing the error:
* Enter the desired error that has to be multiplied to the data on line 24. Default is `INJECT_ERROR = (100 + random.uniform(-.5,.5))`

* Multiply the error by adding `* error` at the end of lines 49 to 52 as desired. By default, at line 52,  `alpha=(float((row[20]).strip())) * error` is present, introducing the error only to the value of `alpha`. 

###### Selecting data to be sent to PILOTS server:
* Send the desired data to PILOTS by editing line 60. By default, line 60 contains `data = ":"+date+" "+ hour+mint+sec+msec+"-0500:"+str(alpha)+','+str(v_t)+ '\r\n'`, which sends only `alpha` and `v_t`.

* You also need to adjust the string `first` on line 31 accordingly. Default content is `first="#aoa,v" + '\r\n'`.

* The `"-0500:"` on line 60 may be changed to represent the desired time zone.

###### Setting adress of PILOTS server and changing the frequency of data transfer
* Enter the IP and port of the PILOTS server on line 30. The default value is `s.connect(('127.0.0.1', 8888))`.

* The frequency at which new data is transferred can be set at line 64. Default value is `time.sleep(1.0)`, since Xplane updates the `Data.txt` file every one second.

##### Instructions for using the code:
* `python 2.xxx` is required to run the code.

* Put the code in the main folder of Xplane where the generated `Data.txt` file is present. Then start PILOTS server, start Xplane, open a terminal at the directory where the code is present, type `python xplaneDataToPilotsTcp.py` and hit `enter`.

* To __start injecting error__, type `1` in the console window where `xplaneDataToPilotsTcp.py` is running and press `enter`.

* To __stop injecting error__, type `2` in the console window where `xplaneDataToPilotsTcp.py` is running and press `enter`.
 

##### DISCLAIMER: 
Copyright &copy; 2019 Saswata Paul

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

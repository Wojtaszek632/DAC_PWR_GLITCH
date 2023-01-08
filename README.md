Quick scritp used to power glitch AVR microcontrolers into reseting fuse bytes (and thus allowing memory hex dump)
```
python3 ./DAC_UART.py <Voltage in V*100>
```
For example:
```
python3 ./DAC_UART.py 330
```
sets DAC to 3.3 V

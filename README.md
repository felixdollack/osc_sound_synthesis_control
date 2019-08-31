# osc_sound_synthesis_control
Receive commands in form of open sound control messages and control an instance of the Sound Scape Renderer.

## Requirements
The packages python-osc and opti_ssr.

```
pip install python-osc opti-ssr
```

## Example
The easiest use case is just by calling the script.
This will start a server that is listening on port 9000 and the 0.0.0.0 address for osc messages.
Valid messages trigger control commands.
Those commands are forwarded to the instance of Sound Scape Renderer on port 45678 at the localhost.
```
python osc_sound_synthesis_control.py
```

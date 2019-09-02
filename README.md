# osc_sound_synthesis_control
Receive commands in form of open sound control ([OSC]) messages and controls an instance of [Sound Scape Renderer].

## Requirements
The packages [python-osc] and [opti-ssr].

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
These ports and IP addresses are default for the setup this program was used in.
Feel free to change them via the input options.

```
python osc_sound_synthesis_control.py --osc-port <port-value> --osc-ip <ip-address> --ssr-port <port-value> --ssr-ip <ip-address>
```

## Simple Sound Scene
Scenes are expected to be saved in the ssr_scenes folder.
Path to sound sources used in the scene descriptions need to be absolute.
Below is a minimal example. The volume parameter is the master volume.

```
<?xml version="1.0" encoding="utf-8"?>
<asdf>
  <scene-setup>
    <volume>0</volume>
    <source name="Sound">
      <file>/Users/me/sound.wav</file>
      <position x="0.0" y="1.0"/>
    </source>
  </scene-setup>
</asdf>
```

[OSC]:https://en.wikipedia.org/wiki/Open_Sound_Control
[Sound Scape Renderer]:http://spatialaudio.net/ssr/
[python-osc]:https://pypi.org/project/python-osc/
[opti-ssr]:https://pypi.org/project/opti-ssr/

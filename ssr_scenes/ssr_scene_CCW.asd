<?xml version="1.0" encoding="utf-8"?>
<asdf>
  <header> <!-- the header is optional -->
    <name>Counter Clockwise Circle Guidance</name>
    <description>
      The scene has a single noise sound source.
      The position of the sound will be controlled externally.
      The scene is ment to be reproduced with the binaural renderer.
    </description>
  </header>

  <scene_setup>
    <!-- set master volume to -18 dB -->
    <volume>-18</volume>

    <source name="Target">
      <file>/Users/felixdollack/Documents/anticipation/signals/noise.wav</file>
      <position x="0.0" y="0.5"/>
    </source>
  </scene_setup>
</asdf>

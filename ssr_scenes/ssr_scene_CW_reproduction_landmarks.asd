<?xml version="1.0" encoding="utf-8"?>
<asdf>
  <header> <!-- the header is optional -->
    <name>Clockwise Circle Reproduction</name>
    <description>
      The scene is composed of three landmarks.
      The landmarks are sounds of a Cicada,
      a Piano and a male German talker.
      The scene is ment to be reproduced with the binaural renderer.
    </description>
  </header>

  <scene_setup>
    <!-- set master volume to -18 dB -->
    <volume>-18</volume>

    <source name="Cicada">
      <file>/Users/felixdollack/Documents/anticipation/signals/cicada.wav</file>
      <position x="0.0" y="1"/>
    </source>

    <source name="Piano">
      <file>/Users/felixdollack/Documents/anticipation/signals/piano.wav</file>
      <position x="3.48" y="1"/>
    </source>

    <source name="Speech">
      <file>/Users/felixdollack/Documents/anticipation/signals/speech.wav</file>
      <position x="1.74" y="-2"/>
    </source>
  </scene_setup>
</asdf>

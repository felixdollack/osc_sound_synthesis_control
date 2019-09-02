#!/bin/python

import sys, os
from time import sleep

# install with: pip install python-osc
from pythonosc import osc_server, dispatcher

# install with: pip install opti-ssr
from opti_ssr.ssr_client import SSRClient

def print_help():
    print('osc_sound_synthesis_control.py --OPTION --VALUE')
    print('options:')
    print(' * osc-port\n * osc-ip\n * ssr-port\n * ssr-ip\n * debug\n * help')
    exit(1)

def onConnectionChanged(addr, key, value):
    global ssr
    print("connection changed: " + str(addr) + " -> " + str(key) + "=" + str(value))
    # connect
    if ((ssr['client'] == None) and (value == 1)):
        ssr['client'] = SSRClient(ssr['ip'], port=ssr['port'])
    # disconnect
    if ((ssr['client'] != None) and (value == 0)):
        ssr['client']._s.close()

def onPlaybackStateChanged(addr, key, value):
    global ssr
    print("playback state changed: " + str(addr) + " -> " + str(key) + "=" + str(value))
    if (ssr['client'] != None):
        if (value == 1):
            ssr['client'].set_transport_state('start')
        else:
            ssr['client'].set_transport_state('stop')
            ssr['client'].set_transport_state('rewind')

def onListenerOrientationChanged(addr, key, angle):
    global ssr
    print("listener orientation changed: " + str(addr) + " -> " + str(key) + "=" + str(angle))
    if (ssr['client'] != None):
        ssr['client'].set_ref_orientation(angle)

def onListenerPositionChanged(addr, x, y):
    global ssr
    print("listener position changed: " + str(addr) + " -> " + str(x) + "=" + str(y))
    if (ssr['client'] != None):
        ssr['client'].set_ref_position(x, y)

def onTargetSoundPositionChanged(addr, x, y):
    global ssr
    print("sound position changed: " + str(addr) + " -> " + str(x) + "=" + str(y))
    if (ssr['client'] != None):
        ssr['client'].set_src_position(1, x, y)

def loadRenderScene(addr, key, filename):
    global BASE_PATH, ssr
    print("load scene: " + str(addr) + " -> " + str(key) + "=" + str(filename))
    if (ssr['client'] != None):
        path = os.path.abspath(os.path.join(BASE_PATH, 'ssr_scenes', filename + '.asd'))
        ssr['client'].load_scene(path)
    # it takes some time to load a new scene, so wait a little here
    sleep(2)

if __name__ == '__main__':
    # default settings
    DEBUG    = False
    OSC_PORT = 9000
    OSC_IP   = '0.0.0.0'
    SSR_PORT = 45678
    SSR_IP   = 'localhost'

    # check number of input arguments
    argc = len(sys.argv)

    # get path were this script and the rendering scenes are
    BASE_PATH = os.path.dirname(sys.argv[0])

    # process input arguments
    if (argc > 1):
        for kk in range(1, argc, 2):
            CMD = ''
            if (not sys.argv[kk].startswith('--')):
                print('skipping ' + sys.argv[kk] +', unkown argument')
                continue
            else:
                CMD = sys.argv[kk].upper()[2:]
            if (CMD == 'OSC-PORT'):
                OSC_PORT = int(sys.argv[kk+1])
            if (CMD == 'OSC-IP'):
                OSC_IP = int(sys.argv[kk+1])
            if (CMD == 'SSR-PORT'):
                SSR_PORT = int(sys.argv[kk+1])
            if (CMD == 'SSR-IP'):
                SSR_IP = int(sys.argv[kk+1])
            if ((CMD == 'D') or (CMD == 'DEBUG')):
               DEBUG = True
               print(DEBUG)
            if ((CMD == 'H') or (CMD == 'HELP')):
               print_help()

    if (DEBUG == True):
        print(' -- settings --')
        print('| \t PORT\t IP')
        print('| OSC\t', OSC_PORT, '\t', OSC_IP)
        print('| SSR\t', SSR_PORT, '\t', SSR_IP)

    # dictionary to keep data related to sound scape renderer
    ssr = dict()
    ssr['client'] = None
    ssr['ip'] = SSR_IP
    ssr['port'] = SSR_PORT

    # define how to react to incoming osc messages
    eventHandler = dispatcher.Dispatcher()
    eventHandler.map('/connect', onConnectionChanged)
    eventHandler.map('/stream', onPlaybackStateChanged)
    eventHandler.map('/azimuth', onListenerOrientationChanged)
    eventHandler.map('/pos', onListenerPositionChanged)
    eventHandler.map('/soundpos', onTargetSoundPositionChanged)
    eventHandler.map('/load', loadRenderScene)

    # create osc server
    oscServer = osc_server.ThreadingOSCUDPServer((OSC_IP, OSC_PORT), eventHandler)
    oscServer.serve_forever()

#!/usr/bin/env nim
mode = ScriptMode.Verbose


task build, "Builds":
    exec "uv pip install ."
    echo "Here"    

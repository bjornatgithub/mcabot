#!/usr/bin/env python
import com
import control 

# __main__
comm  = com.com_thread()
ctrl  = control.ctrl_thread()

comm.start()
ctrl.start()


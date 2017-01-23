#!/usr/bin/env python
import com
import control 

# __main__
comm  = com.Com()
ctrl  = control.Control()

comm.start()
ctrl.start()


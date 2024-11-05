#!/usr/bin/env python
import spa
import gui
import wx
import fire

def main(cui:bool=False):
    # CUI
    if cui == True:
        # spa.spa(input_file_name="indata_cp.txt", fft_size=32, fs=1.0)
        spa.spa(input_file_name="indata_cp.txt", fft_size=32, fs=1.0, target_figure_displayed=spa.Traces.FOURIER_COEFFICIENT, target_file_stored=spa.Traces.NONE)
        return
    
    # GUI
    app = wx.App(False)
    frame = gui.gui(None)
    frame.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    fire.Fire(main)
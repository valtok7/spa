#!/usr/bin/env python
import spa_core
import spa_gui
import wx
import fire
import os

def main(cui:bool=False):
    # CUI
    if cui == True:
        spa = spa_core.SPA()
        spa.analyze(input_file_name="indata_cp.txt", fft_size=32, fs=1.0, target_figure_displayed=spa_core.Traces.FOURIER_COEFFICIENT, target_file_stored=spa_core.Traces.NONE)
        return
    
    # GUI
    app = wx.App(False)
    frame = spa_gui.gui(None)
    dirname = os.path.dirname(os.path.abspath(__file__))
    icon = wx.Icon(f"{dirname}/spa.ico", wx.BITMAP_TYPE_ICO)
    frame.SetIcon(icon)
    frame.Show(True)
    app.MainLoop()

if __name__ == "__main__":
    fire.Fire(main)
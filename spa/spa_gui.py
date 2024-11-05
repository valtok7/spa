# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 4.2.1-0-g80c4cb6)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

import gettext
_ = gettext.gettext

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = _(u"spa"), pos = wx.DefaultPosition, size = wx.Size( 570,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, _(u"Input File"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )

        self.m_staticText2.SetMinSize( wx.Size( 100,-1 ) )

        bSizer2.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_inputFileName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_inputFileName, 1, wx.ALL, 5 )

        self.m_brouseInputFileName = wx.Button( self, wx.ID_ANY, _(u"Brouse"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_brouseInputFileName, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer2, 0, wx.EXPAND, 5 )

        bSizer3 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_fileType = wx.StaticText( self, wx.ID_ANY, _(u"File Format"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_fileType.Wrap( -1 )

        self.m_fileType.SetMinSize( wx.Size( 100,-1 ) )

        bSizer3.Add( self.m_fileType, 0, wx.ALL, 5 )

        m_fileFormatChoices = [ _(u"Real CSV"), _(u"Complex CSV") ]
        self.m_fileFormat = wx.ComboBox( self, wx.ID_ANY, _(u"Real CSV"), wx.DefaultPosition, wx.DefaultSize, m_fileFormatChoices, 0 )
        bSizer3.Add( self.m_fileFormat, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer3, 0, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, _(u"FFT Size"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        self.m_staticText3.SetMinSize( wx.Size( 100,-1 ) )

        bSizer6.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.m_fftSize = wx.TextCtrl( self, wx.ID_ANY, _(u"32"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_fftSize, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer6, 0, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, _(u"Window"), wx.DefaultPosition, wx.Size( 100,-1 ), 0 )
        self.m_staticText9.Wrap( -1 )

        bSizer11.Add( self.m_staticText9, 0, wx.ALL, 5 )

        m_windowTypeChoices = [ _(u"Rectangular"), _(u"Hanning"), _(u"Hamming"), _(u"Blackman"), _(u"Blackman-Harris") ]
        self.m_windowType = wx.ComboBox( self, wx.ID_ANY, _(u"Rectangular"), wx.DefaultPosition, wx.DefaultSize, m_windowTypeChoices, 0 )
        bSizer11.Add( self.m_windowType, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, _(u"   "), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText10.Wrap( -1 )

        bSizer11.Add( self.m_staticText10, 0, wx.ALL, 5 )

        self.m_staticText11 = wx.StaticText( self, wx.ID_ANY, _(u"Window Correction Type"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        bSizer11.Add( self.m_staticText11, 0, wx.ALL, 5 )

        m_windowCorrectionTypeChoices = [ _(u"No Correction"), _(u"Amplitude"), _(u"Power") ]
        self.m_windowCorrectionType = wx.ComboBox( self, wx.ID_ANY, _(u"Amplitude"), wx.DefaultPosition, wx.DefaultSize, m_windowCorrectionTypeChoices, 0 )
        bSizer11.Add( self.m_windowCorrectionType, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer11, 0, wx.EXPAND, 5 )

        bSizer7 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, _(u"Sampling Rate"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText4.Wrap( -1 )

        self.m_staticText4.SetMinSize( wx.Size( 100,-1 ) )

        bSizer7.Add( self.m_staticText4, 0, wx.ALL, 5 )

        self.m_samplingRate = wx.TextCtrl( self, wx.ID_ANY, _(u"1.0"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer7.Add( self.m_samplingRate, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer7, 0, wx.EXPAND, 5 )

        bSizer71 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText5 = wx.StaticText( self, wx.ID_ANY, _(u"Power Spectrum (dB)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText5.Wrap( -1 )

        self.m_staticText5.SetMinSize( wx.Size( 150,-1 ) )

        bSizer71.Add( self.m_staticText5, 0, wx.ALL, 5 )

        self.m_powerSpectrumPlot = wx.CheckBox( self, wx.ID_ANY, _(u"Plot"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_powerSpectrumPlot.SetValue(True)
        bSizer71.Add( self.m_powerSpectrumPlot, 0, wx.ALL, 5 )

        self.m_powerSpectrumFile = wx.CheckBox( self, wx.ID_ANY, _(u"File"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_powerSpectrumFile.SetValue(True)
        bSizer71.Add( self.m_powerSpectrumFile, 0, wx.ALL, 5 )

        self.m_spectrumSwap = wx.CheckBox( self, wx.ID_ANY, _(u"Spectrum Swap"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_spectrumSwap.SetValue(True)
        bSizer71.Add( self.m_spectrumSwap, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer71, 0, wx.EXPAND, 5 )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText6 = wx.StaticText( self, wx.ID_ANY, _(u"Fourier Coefficient"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText6.Wrap( -1 )

        self.m_staticText6.SetMinSize( wx.Size( 150,-1 ) )

        bSizer8.Add( self.m_staticText6, 0, wx.ALL, 5 )

        self.m_fourierCoefficientPlot = wx.CheckBox( self, wx.ID_ANY, _(u"Plot"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_fourierCoefficientPlot.SetValue(True)
        bSizer8.Add( self.m_fourierCoefficientPlot, 0, wx.ALL, 5 )

        self.m_fourierCoefficientFile = wx.CheckBox( self, wx.ID_ANY, _(u"File"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_fourierCoefficientFile.SetValue(True)
        bSizer8.Add( self.m_fourierCoefficientFile, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer8, 0, wx.EXPAND, 5 )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText7 = wx.StaticText( self, wx.ID_ANY, _(u"Power vs Time (dB)"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText7.Wrap( -1 )

        self.m_staticText7.SetMinSize( wx.Size( 150,-1 ) )

        bSizer9.Add( self.m_staticText7, 0, wx.ALL, 5 )

        self.m_powerVsTimePlot = wx.CheckBox( self, wx.ID_ANY, _(u"Plot"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_powerVsTimePlot.SetValue(True)
        bSizer9.Add( self.m_powerVsTimePlot, 0, wx.ALL, 5 )

        self.m_powerVsTimeFile = wx.CheckBox( self, wx.ID_ANY, _(u"File"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_powerVsTimeFile.SetValue(True)
        bSizer9.Add( self.m_powerVsTimeFile, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer9, 0, wx.EXPAND, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, _(u"IQ vs Time"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText8.Wrap( -1 )

        self.m_staticText8.SetMinSize( wx.Size( 150,-1 ) )

        bSizer10.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_iqVsTimePlot = wx.CheckBox( self, wx.ID_ANY, _(u"Plot"), wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_iqVsTimePlot.SetValue(True)
        bSizer10.Add( self.m_iqVsTimePlot, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer10, 0, wx.EXPAND, 5 )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        self.m_execute = wx.Button( self, wx.ID_ANY, _(u"execute"), wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.m_execute, 0, wx.ALL, 5 )


        bSizer1.Add( bSizer4, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_brouseInputFileName.Bind( wx.EVT_BUTTON, self.onButtonClickBrouseInputFileName )
        self.m_execute.Bind( wx.EVT_BUTTON, self.onButtonClickExecute )

    def __del__( self ):
        pass


    # Virtual event handlers, override them in your derived class
    def onButtonClickBrouseInputFileName( self, event ):
        event.Skip()

    def onButtonClickExecute( self, event ):
        event.Skip()



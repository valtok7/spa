import wx
import spa_core
import json
from spa_gui_builderMyFrame1 import spa_gui_builderMyFrame1

class gui( spa_gui_builderMyFrame1 ):
    def __init__( self, parent ):
        spa_gui_builderMyFrame1.__init__( self, parent )
        self.spa = spa_core.SPA()
        self.config_file = 'spa_config.json'
        self.load_parameters()
        self.UpdateComponents()
        self.Bind(wx.EVT_CLOSE, self.on_close)

    def load_parameters(self):
        try:
            with open(self.config_file, 'r') as f:
                config = json.load(f)
                self.m_inputFileName.Value = config.get('input_file', '')
                self.m_fileFormat.SetValue(config.get('file_format', 'Real CSV'))
                self.m_fftSize.SetValue(str(config.get('fft_size', '1024')))
                self.m_windowType.SetValue(str(config.get('window_type', 'Rectangular')))
                self.m_windowCorrectionType.SetValue(str(config.get('window_correction_type', 'Amplitude')))
                self.m_rbwBandwidth.SetValue(str(config.get('rbw_bandwidth', '0.1')))
                self.m_samplingRate.SetValue(str(config.get('sampling_rate', '1.0')))
                self.m_powerSpectrumPlot.SetValue(bool(config.get('power_spectrum_plot', True)))
                self.m_powerSpectrumFile.SetValue(bool(config.get('power_spectrum_file', True)))
                self.m_spectrumSwap.SetValue(bool(config.get('spectrum_swap', True)))
                self.m_fourierCoefficientPlot.SetValue(bool(config.get('fourier_coefficient_plot', True)))
                self.m_fourierCoefficientFile.SetValue(bool(config.get('fourier_coefficient_file', True)))
                self.m_powerVsTimePlot.SetValue(bool(config.get('power_vs_time_plot', True)))
                self.m_powerVsTimeFile.SetValue(bool(config.get('power_vs_time_file', True)))
                self.m_iqVsTimePlot.SetValue(bool(config.get('iq_vs_time_plot', True)))
        except FileNotFoundError:
            pass  # 初回起動時はファイルが存在しないため、デフォルト値を使用

    def save_parameters(self):
        config = {
            'input_file': self.m_inputFileName.Value,
            'file_format': self.m_fileFormat.GetValue(),
            'fft_size': self.m_fftSize.GetValue(),
            'window_type': self.m_windowType.GetValue(),
            'window_correction_type': self.m_windowCorrectionType.GetValue(),
            'rbw_bandwidth': self.m_rbwBandwidth.GetValue(),
            'sampling_rate': self.m_samplingRate.GetValue(),
            'power_spectrum_plot': self.m_powerSpectrumPlot.GetValue(),
            'power_spectrum_file': self.m_powerSpectrumFile.GetValue(),
            'spectrum_swap': self.m_spectrumSwap.GetValue(),
            'fourier_coefficient_plot': self.m_fourierCoefficientPlot.GetValue(),
            'fourier_coefficient_file': self.m_fourierCoefficientFile.GetValue(),
            'power_vs_time_plot': self.m_powerVsTimePlot.GetValue(),
            'power_vs_time_file': self.m_powerVsTimeFile.GetValue(),
            'iq_vs_time_plot': self.m_iqVsTimePlot.GetValue(),
        }
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=4)
    
    def on_close(self, event):
        self.save_parameters()
        event.Skip()  # イベントを伝播させて、ウィンドウを実際に閉じる

    def onButtonClickBrouseInputFileName( self, event ):
        dialog = wx.FileDialog(None, "Select input file", style=wx.FD_OPEN)        
        if dialog.ShowModal() == wx.ID_OK:
            self.m_inputFileName.Value = dialog.GetPath()

    def OnComboboxWindowType( self, event ):
        # 他のコンポーネントへの影響を反映
        self.UpdateComponents()

    def OnTextRbwBandwidth( self, event ):
        # 他のコンポーネントへの影響を反映
        self.UpdateComponents()
    
    def UpdateComponents(self):
        # Update FFT size, RBW Bandwidth
        match self.m_windowType.GetValue():
            case "RBW 3dB":
                self.m_fftSize.Enable(False)
                require_size:int = spa_core.require_size_for_rbw_3db(float(self.m_samplingRate.GetValue()), float(self.m_rbwBandwidth.GetValue()))
                self.m_fftSize.SetValue(str(require_size))
                self.m_rbwBandwidth.Enable(True)
            case _:
                self.m_fftSize.Enable(True)
                self.m_rbwBandwidth.Enable(False)
        
    def onButtonClickExecute( self, event ):
        # 範囲内に丸める
        if int(self.m_fftSize.GetValue()) <= 0:
            self.m_fftSize.SetValue("8")
        if float(self.m_samplingRate.GetValue()) <= 0.0:
            self.m_samplingRate.SetValue("1.0")
        if float(self.m_rbwBandwidth.GetValue()) <= 0.0:
            self.m_rbwBandwidth.SetValue("0.1")

        # 他のコンポーネントへの影響を反映
        self.UpdateComponents()

        # File Format取得
        file_format:spa_core.FileFormat = spa_core.FileFormat.REAL_CSV
        match self.m_fileFormat.GetValue():
            case "Real CSV":
                file_format = spa_core.FileFormat.REAL_CSV
            case "Complex CSV":
                file_format = spa_core.FileFormat.COMPLEX_CSV
            case "Real BIN":
                file_format = spa_core.FileFormat.REAL_BIN
            case "Complex BIN":
                file_format = spa_core.FileFormat.COMPLEX_BIN
            case _:
                raise ValueError(f"Unknown file format: {self.m_fileFormat.GetValue()}")
        
        # FFT Size取得
        fft_size = int(self.m_fftSize.GetValue())

        # Window Type取得    
        match self.m_windowType.GetValue():
            case "Rectangular":
                window_type = spa_core.WindowType.RECTANGULAR
            case "Blackman-Harris":
                window_type = spa_core.WindowType.BLACKMAN_HARRIS
            case "Hanning":
                window_type = spa_core.WindowType.HANNING
            case "Hamming":
                window_type = spa_core.WindowType.HAMMING
            case "Blackman":
                window_type = spa_core.WindowType.BLACKMAN
            case "RBW 3dB":
                window_type = spa_core.WindowType.RBW_3DB
            case _:
                raise ValueError(f"Unknown correction type: {self.m_windowType.GetValue()}")
            
        # Window Correction Type取得
        window_correction_type:spa_core.WindowCorrectionType = spa_core.WindowCorrectionType.NO_CORRECTION
        if self.m_windowCorrectionType.GetValue() == "Amplitude":
            window_correction_type = spa_core.WindowCorrectionType.AMPLITUDE
        elif self.m_windowCorrectionType.GetValue() == "Power":
            window_correction_type = spa_core.WindowCorrectionType.POWER

        # RBW bandwidth取得
        rbw_band_width = float(self.m_rbwBandwidth.GetValue())

        # Sampling Rate取得
        fs = float(self.m_samplingRate.GetValue())

        # Target Figure Dispalyed取得
        target_figure_displayed:spa_core.Traces = spa_core.Traces.NONE
        if self.m_powerSpectrumPlot.GetValue() == True:
            target_figure_displayed = target_figure_displayed | spa_core.Traces.SPECTRUM_DB
        if self.m_fourierCoefficientPlot.GetValue() == True:
            target_figure_displayed = target_figure_displayed | spa_core.Traces.FOURIER_COEFFICIENT
        if self.m_powerVsTimePlot.GetValue() == True:
            target_figure_displayed = target_figure_displayed | spa_core.Traces.POWER_VS_TIME_DB
        if self.m_iqVsTimePlot.GetValue() == True:
            target_figure_displayed = target_figure_displayed | spa_core.Traces.AMPLITUDE_VS_TIME
        
        # Target File Stored取得
        target_file_stored:spa_core.Traces = spa_core.Traces.NONE
        if self.m_powerSpectrumFile.GetValue() == True:
            target_file_stored = target_file_stored | spa_core.Traces.SPECTRUM_DB
        if self.m_fourierCoefficientFile.GetValue() == True:
            target_file_stored = target_file_stored | spa_core.Traces.FOURIER_COEFFICIENT
        if self.m_powerVsTimeFile.GetValue() == True:
            target_file_stored = target_file_stored | spa_core.Traces.POWER_VS_TIME_DB

        # 解析実行
        self.spa.analyze(input_file_name=self.m_inputFileName.GetValue(), file_format=file_format, fft_size=fft_size, fs=fs, window_type=window_type, window_correction_type=window_correction_type, rbw_band_width=rbw_band_width, spectrum_swap=self.m_spectrumSwap.GetValue(), target_figure_displayed=target_figure_displayed, target_file_stored=target_file_stored)
 
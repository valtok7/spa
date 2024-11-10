import numpy as np
import scipy.fft as fft
import matplotlib.pyplot as plt
import matplotlib.backends.backend_tkagg
import matplotlib.backends.backend_wxagg
import math
from enum import Enum, Flag, auto
from typing import Tuple

# 窓関数
class WindowType(Enum):
    RECTANGULAR = auto()
    HANNING = auto()
    HAMMING = auto()
    BLACKMAN = auto()
    BLACKMAN_HARRIS = auto()
    RBW_3DB = auto()

# 窓関数を作成する
def create_window(window_type: WindowType, window_size: int, fs:float=1.0, rbw_band_width: float=0.1) -> np.ndarray[np.float64]:
    '''
    fs and band_width are for RBW_3DB
    '''
    match window_type:
        case WindowType.RECTANGULAR:
            return np.ones(window_size)
        case WindowType.HANNING:
            return np.hanning(window_size)
        case WindowType.HAMMING:
            return np.hamming(window_size)
        case WindowType.BLACKMAN:
            return np.blackman(window_size)
        case WindowType.BLACKMAN_HARRIS:
            return np.blackman(window_size)
        case WindowType.RBW_3DB:
            return create_window_rbw_3db(window_size=window_size, fs=fs, band_width=rbw_band_width)
        case _:
            raise ValueError(f"Unknown window type: {window_type}")

def create_window_rbw_3db(window_size:int, fs:float, band_width:float) -> np.ndarray[np.float64]:
    a = np.arange(-(window_size - 1)/2.0, (window_size - 1)/2.0 + 1)
    return (1.0/(math.sqrt(2*math.pi*math.log(2.0))/(math.pi*band_width))) * np.exp(-a**2/(2.0*math.log(2.0)/((math.pi**2)*(band_width**2))))

# 窓関数補正係数種別
class WindowCorrectionType(Enum):
    NO_CORRECTION = auto()
    POWER = auto()
    AMPLITUDE = auto()

# 窓関数正係数を算出する
def calc_window_correction_factor(correction_type:WindowCorrectionType, window: np.ndarray[np.float64]) -> float:
    match correction_type:
        case WindowCorrectionType.NO_CORRECTION:
            return 1.0
        case WindowCorrectionType.POWER:
            # 窓関数の2乗平均平方根を計算
            return np.sqrt(np.mean(window ** 2))
        case WindowCorrectionType.AMPLITUDE:
            # 窓関数の2平均を計算
            return np.mean(window)
        case _:
            raise ValueError(f"Unknown correction type: {correction_type}")

# RBW 3dBに必要な信号長を返す
def require_size_for_rbw_3db(fs:float, band_width:float) -> int:
    if band_width <= 0:
        return 8
    require_size:int = int(fs / band_width)
    if require_size < 8:
        require_size = 8   # 最低でも8サンプル使用する
    return require_size

# signalに対してfftを行い、結果をfourier_coefficientに格納する
def calc_fourier_coefficient(signal: np.ndarray[np.complex128], fft_size: int, swap:bool=False, fs:float=1.0) -> Tuple[np.ndarray[np.complex128], np.ndarray[np.float64], np.ndarray[np.float64]]:
    # signalのfftを行い、結果をfourier_coefficientに格納する
    fourier_coefficient:np.ndarray[np.complex128] = fft.fft(signal, fft_size)
    # 1sampleあたりの値とするためfourier_coefficientをfft_sizeで割る
    fourier_coefficient = fourier_coefficient / fft_size
    # swapがTrueの場合、fourier_coefficientの前半と後半を入れ替える
    if swap:
        fourier_coefficient = fft.fftshift(fourier_coefficient)
        if fft_size % 2 == 0:
            freq = np.linspace(-fs/2, fs/2-(fs/fft_size), fft_size)
        else:
            freq = np.linspace(-fs/2+(fs/(fft_size*2)), fs/2-(fs/(fft_size*2)), fft_size)
    else:
        freq = np.linspace(0, fs-(fs/fft_size), fft_size)
    # power spectrum算出
    spectrum_db:np.ndarray[np.float64] = 20 * np.log10(np.abs(fourier_coefficient))
    return fourier_coefficient, spectrum_db, freq

# スペクトラムのグラフを作成する
def plot_spectrum_db(power_spectrum_db: np.ndarray[np.float64], freq: np.ndarray[np.float64], fs:float=1.0) -> None:
    # グラフ表示する
    plt.figure()
    plt.plot(freq, power_spectrum_db)
    plt.minorticks_on()
    plt.grid(which="major", color="gray", linestyle="solid")
    plt.grid(which="minor", color="lightgray", linestyle="dotted")
    plt.xlabel(f"Frequency (Fs={fs})")
    plt.ylabel("Amplitude (dB)")
    plt.title("Spectrum")

# フーリエ係数のグラフを作成する
def plot_fourier_coefficient(fourier_coefficient: np.ndarray[np.complex128], freq: np.ndarray[np.float64], fs:float=1.0) -> None:
    plt.figure()
    plt.plot(freq, np.real(fourier_coefficient), label="Real")
    plt.plot(freq, np.imag(fourier_coefficient), label="Imaginary") 
    plt.minorticks_on()
    plt.grid(which="major", color="gray", linestyle="solid")
    plt.grid(which="minor", color="lightgray", linestyle="dotted")
    plt.xlabel(f"Frequency (Fs={fs})")
    plt.ylabel("Amplitude")
    plt.title("Fourier Coefficient")
    plt.legend()

# Power vs Time(dB)の計算
def calc_power_vs_time_db(signal: np.ndarray[np.complex128], fs:float=1.0) -> np.ndarray[np.float64]:
    # パワーをdBに変換する
    power_db = 20 * np.log10(np.abs(signal))
    return power_db

# Power vs Time(dB)グラフを作成する
def plot_power_vs_time_db(power_db: np.ndarray[np.float64], fs:float=1.0) -> None:
    # 時間軸を作成
    time = np.arange(len(power_db)) / fs
    # グラフ表示する
    plt.figure()
    plt.plot(time, power_db)
    plt.minorticks_on()
    plt.grid(which="major", color="gray", linestyle="solid")
    plt.grid(which="minor", color="lightgray", linestyle="dotted")
    plt.xlabel(f"Time (length={len(power_db)}sample)")
    plt.ylabel("Power (dB)")
    plt.title("Power vs Time")

# Amplitude vs Timeグラフを作成する
def plot_amplitude_vs_time(signal: np.ndarray[np.complex128], fs:float=1.0)-> None:
    # 時間軸を作成
    time = np.arange(len(signal)) / fs
    # グラフ表示する
    plt.figure()
    plt.plot(time, np.real(signal), label="Real")
    plt.plot(time, np.imag(signal), label="Imaginary")
    plt.minorticks_on()
    plt.grid(which="major", color="gray", linestyle="solid") 
    plt.grid(which="minor", color="lightgray", linestyle="dotted")
    plt.xlabel(f"Time (length={len(signal)}sample)")
    plt.ylabel("Amplitude")
    plt.title("Amplitude vs Time")
    plt.legend()

# 対象とレース（ビット和で表現）
class Traces(Flag):
    NONE = 0
    FOURIER_COEFFICIENT = auto()
    SPECTRUM_DB = auto()
    POWER_VS_TIME_DB = auto()
    AMPLITUDE_VS_TIME = auto()

def all_traces() -> Traces:
    all_traces = Traces(0)
    for figure in Traces:
        if figure != Traces.NONE:
            all_traces |= figure
    return all_traces

# グラフ表示する
def plot(signal:np.ndarray[np.complex128], fourier_coefficient: np.ndarray[np.complex128], freq: np.ndarray[np.float64], fs:float=1.0, target_figure_displayed:int=all_traces()) -> None:
    if (target_figure_displayed & Traces.FOURIER_COEFFICIENT) != 0:
        plot_fourier_coefficient(fourier_coefficient=fourier_coefficient, freq=freq, fs=fs)
    if (target_figure_displayed & Traces.SPECTRUM_DB) != 0:
        plot_spectrum_db(fourier_coefficient=fourier_coefficient, freq=freq, fs=fs)
    if (target_figure_displayed & Traces.POWER_VS_TIME_DB) != 0:
        plot_power_vs_time_db(power_db=signal, fs=fs)
    if (target_figure_displayed & Traces.AMPLITUDE_VS_TIME) != 0:
        plot_amplitude_vs_time(signal=signal, fs=fs)

    # グラフを描画する
    plt.show()

# File format
class FileFormat(Enum):
    REAL_CSV = auto()
    COMPLEX_CSV = auto()
    REAL_BIN = auto()       # Binary (float32)
    COMPLEX_BIN = auto()    # Binary (I=float32, Q=float32)

# Real csvデータ読み込み、虚部を0として複素数配列を作成
def read_real_csv(file_name:str, length:int=0, offset:int=0) -> np.ndarray[np.complex128]:
    # 実部のみのcsvファイルを読み込む
    real_signal:np.ndarray[np.float64] = np.loadtxt(file_name)

    # offsetとlengthに基づいてスライス
    if length > 0:
        real_signal = real_signal[offset:offset+length]
    elif offset > 0:
        real_signal = real_signal[offset:]

    # 虚部を0として複素数配列を作成
    signal:np.ndarray[np.complex128] = real_signal + 0j
    return signal

# Complex csvデータ読み込み
def read_complex_csv(file_name:str, length:int=0, offset:int=0) -> np.ndarray[np.complex128]:
    # 実部と虚部を含むcsvファイルを読み込む
    data = np.loadtxt(file_name, delimiter=",")

    # offsetとlengthに基づいてスライス
    if length > 0:
        data = data[offset:offset+length]
    elif offset > 0:
        data = data[offset:]

    # 実部と虚部を結合して複素数配列を作成
    signal:np.ndarray[np.complex128] = data[:,0] + 1j * data[:,1]
    return signal

# Real binary(float32)データ読み込み
def read_real_bin(file_name:str, length:int=0, offset:int=0) -> np.ndarray[np.complex128]:
    # 32bit floatバイナリファイルを読み込む
    real_signal:np.ndarray[np.float32] = np.fromfile(file_name, dtype=np.float32)

    # offsetとlengthに基づいてスライス
    if length > 0:
        real_signal = real_signal[offset:offset+length]
    elif offset > 0:
        real_signal = real_signal[offset:]

    # 虚部を0として複素数配列を作成
    signal:np.ndarray[np.complex128] = real_signal.astype(np.float64) + 0j
    return signal

# Complex binary(float32)データ読み込み
def read_complex_bin(file_name:str, length:int=0, offset:int=0) -> np.ndarray[np.complex128]:
    # 32bit floatバイナリファイルを読み込む
    data:np.ndarray[np.float32] = np.fromfile(file_name, dtype=np.float32)

    # offsetとlengthに基づいてスライス
    if length > 0:
        data = data[offset*2:offset*2+length*2]  # 実部と虚部で2倍のデータ数
    elif offset > 0:
        data = data[offset*2:]

    # 実部と虚部を分離して複素数配列を作成
    real_part = data[0::2].astype(np.float64)  # 偶数インデックスのデータ
    imag_part = data[1::2].astype(np.float64)  # 奇数インデックスのデータ
    signal:np.ndarray[np.complex128] = real_part + 1j * imag_part
    return signal

# Float csvデータ保存
def save_float_csv(file_name:str, data:np.ndarray[np.float64]) -> None:
    # csvファイルに保存
    np.savetxt(file_name, data, delimiter=",")

# Complex csvデータ保存
def save_complex_csv(file_name:str, data:np.ndarray[np.complex128]) -> None:
    # 実部と虚部を分離
    real_part = np.real(data)
    imag_part = np.imag(data)
    # 実部と虚部を結合
    merged_data = np.column_stack((real_part, imag_part))
    # csvファイルに保存
    np.savetxt(file_name, merged_data, delimiter=",")

class SPA():
    # constractor
    def __init__(self):
        pass

    def analyze(self, input_file_name:str, file_format:FileFormat, fft_size:int, fft_offset:int=0, fs:float=1.0, rbw_band_width:float=0.1, window_type:WindowType=WindowType.RECTANGULAR, window_correction_type:WindowCorrectionType=WindowCorrectionType.AMPLITUDE, spectrum_swap:bool=True, target_figure_displayed:int=all_traces(), target_file_stored:int=all_traces()) -> None:
        # ファイル読み込み
        match file_format:
            case FileFormat.REAL_CSV:
                signal:np.ndarray[np.complex128] = read_real_csv(file_name=input_file_name, length=fft_size, offset=fft_offset)
            case FileFormat.COMPLEX_CSV:
                signal:np.ndarray[np.complex128] = read_complex_csv(file_name=input_file_name, length=fft_size, offset=fft_offset)
            case FileFormat.REAL_BIN:
                signal:np.ndarray[np.complex128] = read_real_bin(file_name=input_file_name, length=fft_size, offset=fft_offset)
            case FileFormat.COMPLEX_BIN:
                signal:np.ndarray[np.complex128] = read_complex_bin(file_name=input_file_name, length=fft_size, offset=fft_offset)
            case _:
                raise ValueError(f"Unknown file format: {file_format}")
        
        # Spectrum系トレース
        if (target_figure_displayed & (Traces.FOURIER_COEFFICIENT | Traces.SPECTRUM_DB)) | (target_file_stored & (Traces.FOURIER_COEFFICIENT | Traces.SPECTRUM_DB)) != Traces.NONE:
            # 窓関数を適用する
            window_power_correction_factor:float = 1.0
            if window_type == WindowType.RECTANGULAR:
                signal_windowed = signal
            else:
                window = create_window(window_type=window_type, window_size=len(signal), fs=fs, rbw_band_width=rbw_band_width)
                window_correction_factor = calc_window_correction_factor(window_correction_type, window)
                signal_windowed:np.ndarray[np.complex128] = signal * window / window_correction_factor

            # FFT実行
            fourier_coefficient, power_spectrum_db, freq = calc_fourier_coefficient(signal=signal_windowed, fft_size=fft_size, swap=spectrum_swap, fs=fs)
            # トレース準備
            if (target_figure_displayed & Traces.FOURIER_COEFFICIENT) != Traces.NONE:
                plot_fourier_coefficient(fourier_coefficient=fourier_coefficient, freq=freq, fs=fs)
            if (target_figure_displayed & Traces.SPECTRUM_DB) != Traces.NONE:
                plot_spectrum_db(power_spectrum_db=power_spectrum_db, freq=freq, fs=fs)
            # ファイル保存
            if (target_file_stored & Traces.FOURIER_COEFFICIENT) != Traces.NONE:
                save_complex_csv(file_name="fourier_coefficient.csv", data=fourier_coefficient)
            if (target_file_stored & Traces.SPECTRUM_DB) != Traces.NONE:
                save_float_csv(file_name="power_spectrum_db.csv", data=power_spectrum_db)
        
        # Powre vs Timeトレース
        if (target_figure_displayed & Traces.POWER_VS_TIME_DB) | (target_file_stored & Traces.POWER_VS_TIME_DB) != Traces.NONE:
            # Power vs Time計算
            power_db = calc_power_vs_time_db(signal=signal, fs=fs)
            # トレース準備
            if target_figure_displayed & Traces.POWER_VS_TIME_DB:
                plot_power_vs_time_db(power_db=power_db, fs=fs)
            # ファイル保存
            if target_file_stored & Traces.POWER_VS_TIME_DB:
                save_float_csv(file_name="power_vs_time_db.csv", data=power_db)

        # Amplitude vs Timeトレース（ファイル保存機能なし）
        if (target_figure_displayed & Traces.AMPLITUDE_VS_TIME) != Traces.NONE:
            # トレース準備
            plot_amplitude_vs_time(signal=signal, fs=fs)
            
        # グラフを描画する
        plt.show()



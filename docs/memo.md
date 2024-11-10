cd d:\code\spa
pipenv --python 3.11
pipenv install numpy scipy matplotlib
code .

$$ g(t)=\frac{1}{\sqrt{2\pi}\sigma}\exp(-\frac{t^2}{2\sigma^2})$$
$$ G(f)=\exp(-\frac{\sigma^2(2\pi f)^2}{2})$$

3dB帯域幅=Bの場合
$$ \exp(-\frac{\sigma^2(2\pi \frac{B}{2})^2}{2})=\frac{1}{\sqrt{2}}$$
$$ \ln\{\exp(-\frac{\sigma^2(2\pi \frac{B}{2})^2}{2})\}=\ln(\frac{1}{\sqrt{2}})$$
$$ -\frac{\sigma^2(2\pi \frac{B}{2})^2}{2}=-\frac{\ln2}{2}$$
$$ \sigma^2(2\pi \frac{B}{2})^2=\ln2$$
$$ \sigma^2=\frac{\ln2}{\pi^2 B^2}$$
$$ \sigma=\frac{\sqrt{\ln2}}{\pi B}$$
すなわち
$$ g(t)=\frac{1}{\sqrt{2\pi}\frac{\sqrt{\ln2}}{\pi B}}\exp(-\frac{t^2}{2\frac{\ln2}{\pi^2 B^2}})$$
$$ =\frac{\sqrt{\pi} B}{\sqrt{2\ln2}}\exp(-\frac{\pi^2 B^2 t^2}{2\ln2})$$
$$ G(f)=\exp(-\frac{\frac{\ln2}{\pi^2 B^2}(2\pi f)^2}{2})$$
$$ =\exp(-\frac{2(\ln2) f^2}{B^2})$$
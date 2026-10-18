"""Original synthesized 120 BPM score. No samples or borrowed melody."""
from pathlib import Path
import numpy as np, wave
sr=48000; duration=25; n=sr*duration
out=np.zeros((n,2)); rng=np.random.default_rng(101826)
def add(s,start,amp,pan=0):
 st=round(start*sr);l=min(len(s),n-st)
 if l>0:out[st:st+l]+=s[:l,None]*amp*np.array([1-.3*pan,1+.3*pan])
def tone(m,sec,decay=4):
 t=np.arange(round(sec*sr))/sr;h=440*2**((m-69)/12)
 return (np.sin(2*np.pi*h*t)+.25*np.sin(2*np.pi*2*h*t)+.1*np.sin(2*np.pi*3*h*t))*(1-np.exp(-t*150))*np.exp(-decay*t)
chords=[[50,57,62,65],[53,60,65,69],[48,55,60,64],[55,62,67,70]]
for k in range(12):
 st=2*k;c=chords[k%4];t=np.arange(sr*2)/sr
 for j,m in enumerate(c):
  h=440*2**((m-69)/12);s=(np.sin(2*np.pi*h*t)+np.sin(2*np.pi*h*1.002*t))/2
  add(s*np.minimum(t/.15,1)*np.minimum((2-t)/.3,1),st,.035,(j-1.5)/1.5)
 for j in range(8):
  add(tone(c[[0,2,1,3,2,1,3,2][j]]+12,.55,7),st+j*.25,.06 if st<7 else .09,(-1)**j*.7)
for k in range(48):
 st=k*.5;t=np.arange(int(.3*sr))/sr
 add(np.sin(2*np.pi*(46*t+4*(1-np.exp(-t*35))))*np.exp(-t*18),st,.32)
 add(tone(chords[(k//4)%4][0]-12,.35,9),st,.16)
 if k%2:
  t=np.arange(int(.18*sr))/sr;noise=rng.standard_normal(len(t));noise=np.convolve(noise,np.ones(3)/3,'same')
  add(noise*np.exp(-t*30),st,.12)
 if st>=3:
  for off in [0,.25]:
   t=np.arange(int(.06*sr))/sr;no=rng.standard_normal(len(t));no=np.diff(no,prepend=0)
   add(no*np.exp(-t*65),st+off,.025,(-1)**k)
for end in [3.5,7,10.5,14,18,21.5]:
 t=np.arange(int(.6*sr))/sr;no=rng.standard_normal(len(t));no=np.convolve(no,np.ones(9)/9,'same')
 add(no*(t/.6)**2,end-.6,.22,-.4)
 add(tone(38,.8,8),end,.3)
for m in [50,57,62,65,74]:add(tone(m,3.5,1.8),21.5,.1)
t=np.arange(n)/sr;out*=np.minimum(t/.02,1)[:,None]*np.clip((25-t)/1.2,0,1)[:,None]
out=np.tanh(out*1.5);out*=.85/np.max(abs(out))
p=Path(__file__).parent/'composition/assets/original-score.wav'
with wave.open(str(p),'wb') as f:f.setnchannels(2);f.setsampwidth(2);f.setframerate(sr);f.writeframes((out*32767).astype('<i2').tobytes())
print('25 s original stereo score; peak',np.max(abs(out)))

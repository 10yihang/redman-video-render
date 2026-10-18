"""Original procedural score, no sampled or third-party musical material."""
from pathlib import Path
import numpy as np, wave
sr=48000;duration=8;n=sr*duration
out=np.zeros((n,2));rng=np.random.default_rng(817)
def add(sound,start,amp,pan=0):
 st=round(start*sr); length=min(len(sound),n-st)
 if length>0:
  out[st:st+length,0]+=sound[:length]*amp*(1-pan*.25)
  out[st:st+length,1]+=sound[:length]*amp*(1+pan*.25)
def note(midi,sec,decay=4):
 t=np.arange(round(sec*sr))/sr; hz=440*2**((midi-69)/12)
 return (np.sin(2*np.pi*hz*t)+.17*np.sin(2*np.pi*hz*2*t))*(1-np.exp(-t*130))*np.exp(-t*decay)
for start,chord in [(0,[50,57,62,65]),(2,[53,60,65,69]),(4,[48,55,60,64]),(6,[50,57,62,65])]:
 t=np.arange(sr*2)/sr
 for j,m in enumerate(chord):
  hz=440*2**((m-69)/12)
  pad=(np.sin(2*np.pi*hz*t)+np.sin(2*np.pi*hz*1.001*t))*.5
  pad*=np.minimum(t/.2,1)*np.minimum((2-t)/.35,1)
  add(pad,start,.045,(j-1.5)/1.5)
 for k in range(4):
  add(note(chord[k]+12,.8),start+k*.5,.075,(-1)**k*.6)
  add(note(chord[0]-12,.5,7),start+k*.5,.16)
for k in range(16):
 t=np.arange(round(.18*sr))/sr
 kick=np.sin(2*np.pi*(48*t+4*(1-np.exp(-t*40))))*np.exp(-t*25)
 add(kick,k*.5,.19)
 if k%2:
  t=np.arange(round(.08*sr))/sr
  noise=rng.standard_normal(len(t));noise=np.convolve(noise,np.ones(10)/10,'same')
  add(noise*np.exp(-t*60),k*.5,.14,.15)
for time in [.95,1.25,2.85,4.8,5.7,6.15]:
 add(note(76 if time<2 else 81,.4,12),time,.09,.3)
for time in [2.2,4.65]:
 t=np.arange(round(.4*sr))/sr;noise=rng.standard_normal(len(t));noise=np.convolve(noise,np.ones(30)/30,'same')
 add(noise*np.sin(np.pi*t/.4)**2,time,.23,-.3)
t=np.arange(n)/sr;out*=np.minimum(t/.03,1)[:,None]*np.minimum((8-t)/.6,1)[:,None]
out=np.tanh(out*1.3);out*=.68/max(np.abs(out).max(),.01)
p=Path(__file__).parent/'composition/assets/original-score.wav'
with wave.open(str(p),'wb') as f:
 f.setnchannels(2);f.setsampwidth(2);f.setframerate(sr);f.writeframes((out*32767).astype('<i2').tobytes())
print('Original stereo score:',p,'duration=8.000s, peak=',np.abs(out).max())

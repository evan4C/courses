from wave import open
from struct import Struct
from math import floor

# sampling rate: how many times per second do we need have some value 
# to record the amplitude of the wave
frame_rate = 11025

def encode(x):
	"""encode float x between -1 and 1 as two bytes.
	encode integers in the format that WAV files require
	reference https://docs.python.org/3/library/struct.html
	"""
	i = int(16384 * x)
	return Struct('h').pack(i)

def play(sampler, name='song.wav', seconds=2):
	"""write the output of a sampler function as a wav file.
	sampler will generate the amplitude of the wave at time t
	"""
	out = open(name, 'wb')
	out.setnchannels(1)
	out.setsampwidth(2)
	out.setframerate(frame_rate)
	t = 0
	while t < seconds * frame_rate:
		sample = sampler(t)
		out.writeframes(encode(sample))
		t = t + 1
	out.close()

def  tri(frequency, amplitude=0.3):
	"""a continuous triangle wace."""
	
	# calc how many samples are taken in one triangle wave
	period = frame_rate // frequency

	def sampler(t):
		# calc the digit of t
		saw_wave = t / period - floor(t / period + 0.5)
		# clac the wave height
		tri_wave = 2 * abs(2 * saw_wave) - 1
		return amplitude * tri_wave
	return sampler

c_freq, e_freq, g_freq = 261.63, 329.63, 392.00

c = tri(c_freq)
play(c)

def both(f, g):
	return lambda t: f(t) + g(t)

# paly a chord of c and e
play(both(tri(c_freq), tri(e_freq)), name='ce.wav')

def note(f, start, end, fade=0.01):
	"""take a sound F and play it from start to end"""
	def sampler(t):
		seconds = t / frame_rate
		if seconds < start:
			return 0
		elif seconds > end:
			return 0
		elif seconds < start + fade:
			return (seconds - start) / fade * f(t)
		elif seconds > end - fade:
			return (end - seconds) / fade * f(t)
		else:
			return f(t)
	return sampler

c, e = tri(c_freq), tri(e_freq)
g, low_g = tri(g_freq), tri(g_freq / 2)
play(both(note(c, 0, 1/4), note(e, 1/2, 1)), name='note.wav')

z = 0
song = note(e, z, z + 1/8)
z += 1/8
song = both(song, note(e, z, z + 1/8))
z += 1/4
song = both(song, note(e, z, z + 1/8))
z += 1/4
song = both(song, note(c, z, z + 1/8))
z += 1/8
song = both(song, note(e, z, z + 1/8))
z += 1/4
song = both(song, note(g, z, z + 1/8))
z += 1/2
song = both(song, note(low_g, z, z + 1/8))
z += 1/2

play(song, name='mysong.wav')

def mario_at(octave):
	c, e = tri(octave * c_freq), tri(octave * e_freq)
	g, low_g = tri(octave * g_freq), tri(octave * g_freq / 2)
	return mario(c, e, g, low_g)


def mario(c, e, g, low_g):
	z = 0
	song = note(e, z, z + 1/8)
	z += 1/8
	song = both(song, note(e, z, z + 1/8))
	z += 1/4
	song = both(song, note(e, z, z + 1/8))
	z += 1/4
	song = both(song, note(c, z, z + 1/8))
	z += 1/8
	song = both(song, note(e, z, z + 1/8))
	z += 1/4
	song = both(song, note(g, z, z + 1/8))
	z += 1/2
	song = both(song, note(low_g, z, z + 1/8))
	z += 1/2
	return song

play(mario_at(1), name='mario.wav')
play(mario_at(1/2), name='lower_mario.wav')
play(both(mario_at(1), mario_at(1/2)), name='mix_mario.wav')
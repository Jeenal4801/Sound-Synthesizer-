'''from pydub import AudioSegment
import os, wave, numpy
import matplotlib.pyplot as plt
fn_wavi = os.path.join('..', 'data', 'B', 'D:\Programming\Python\BabyElephantWalk60.wav')
song = AudioSegment.from_wav(fn_wavi)
choice=int(input("Do you want to \n"
                 "1) increase volume "
                 "2) decrease volume\n"))
if choice==1:
    n = int(input("By how many dBs you want to increase the volume?\n"))
    song_low = song + n
elif choice==2:
    n = int(input("By how many dBs you want to decrease the volume?\n"))
    song_low = song - n
else:
    print("Invalid choice.")

fn_wavo = os.path.join('..', 'data', 'B', 'D:\Programming\Python\low.wav')
song_low.export(fn_wavo, "wav")
print("Done")
#Graphs
path_origin='D:\Programming\Python\BabyElephantWalk60.wav'
raw = wave.open(path_origin)
signal1 = raw.readframes(-1)
signal1 = numpy.frombuffer(signal1, dtype="int16")
f_rate1 = raw.getframerate()
time1 = numpy.linspace(
    0,
    len(signal1) / f_rate1,
    num=len(signal1)
)
plt.subplot(2,1,1)
plt.figure(1)
plt.title("Input Sound Wave")
plt.xlabel("Time")
plt.plot(time1, signal1)

path='D:\Programming\Python\low.wav'
raw = wave.open(path)
signal = raw.readframes(-1)
signal = numpy.frombuffer(signal, dtype="int16")
f_rate = raw.getframerate()
time = numpy.linspace(
    0,
    len(signal) / f_rate,
    num=len(signal)
)
plt.subplot(2,1,2)
plt.figure(1)
plt.title("Output Sound Wave")
plt.xlabel("Time")
plt.plot(time, signal)
plt.show()'''
'''from pydub import AudioSegment
from mpl_toolkits import mplot3d
import os, wave, numpy
import matplotlib.pyplot as plt
fn_wavi = os.path.join('..', 'data', 'B', 'D:\Programming\Python\BabyElephantWalk60.wav')
song = AudioSegment.from_wav(fn_wavi)
choice=int(input("Do you want to \n"
                 "1) increase volume "
                 "2) decrease volume\n"))
if choice==1:
    n = int(input("By how many dBs you want to increase the volume?\n"))
    song_low = song + n
elif choice==2:
    n = int(input("By how many dBs you want to decrease the volume?\n"))
    song_low = song - n
else:
    print("Invalid choice.")

fn_wavo = os.path.join('..', 'data', 'B', 'D:\Programming\Python\low.wav')
song_low.export(fn_wavo, "wav")
print("Done")
#Graphs
path_origin='D:\Programming\Python\BabyElephantWalk60.wav'
raw = wave.open(path_origin)
signal1 = raw.readframes(-1)
signal1 = numpy.frombuffer(signal1, dtype="int16")
f_rate1 = raw.getframerate()
z = 2
time1 = numpy.linspace(
    0,
    len(signal1) / f_rate1,
    num=len(signal1)
)

fig = plt.figure(figsize=plt.figaspect(0.5))
ax = fig.add_subplot(2, 1, 1, projection='3d')
ax.plot_trisurf(time1, signal1, z,cmap='magma', edgecolor='none');
ax.set_xlabel('Time')
ax.set_ylabel('Signal')
ax.set_zlabel('z');



path='D:\Programming\Python\low.wav'
raw = wave.open(path)
signal = raw.readframes(-1)
signal = numpy.frombuffer(signal, dtype="int16")
z = 2
f_rate = raw.getframerate()
time = numpy.linspace(
    0,
    len(signal) / f_rate,
    num=len(signal)
)
fig = plt.figure(figsize=plt.figaspect(0.5))
ax1 = fig.add_subplot(2, 1, 2, projection='3d')
ax1.plot_trisurf(time, signal, z,cmap='magma', edgecolor='none');
ax1.set_xlabel('Time')
ax1.set_ylabel('Signal')
ax1.set_zlabel('z');'''
from pydub import AudioSegment
import os, wave, numpy
import matplotlib.pyplot as plt
def changeVolume():
    # This is code to increase volume or decrease the volume
    # install  pydub, AudioSegment,os,wave,numpy and matplotlib libraries
    from pydub import AudioSegment
    import os, wave, numpy
    import matplotlib.pyplot as plt
    # Enter a path from where the input file is saved
    given = input("Please enter the path to your file: \n")
    fn_wavi = os.path.join('..', 'data', 'B', given)
    song = AudioSegment.from_wav(fn_wavi)

    # here user will get two choices to increase or decrease the volume
    choice = int(input("Do you want to \n"
                       "1) increase volume "
                       "2) decrease volume\n"))
    # here n is the number for which how many dbs he want to increase or decrease the volume we will add n if to increase and subtract n decrease volume from the song else it will give error of invalid if none choice is selected
    # provide the final path to save the output file
    if choice == 1:
        n = int(input("By how many dBs you want to increase the volume?\n"))
        song_low = song + n
    elif choice == 2:
        n = int(input("By how many dBs you want to decrease the volume?\n"))
        song_low = song - n
    else:
        print("Invalid choice.")
    final = input("Done, Please provide a path to save the file: \n")
    fn_wavo = os.path.join('..', 'data', 'B', final)
    song_low.export(fn_wavo, "wav")

    # Graphs
    # Setting the figure size

    plt.figure(figsize=(10, 6))
    ax = plt.axes()

    # printing graph of input file using matplotlib.pyplot plt function
    path_origin = given
    raw = wave.open(path_origin)
    signal1 = raw.readframes(-1)
    signal1 = numpy.frombuffer(signal1, dtype="int16")
    f_rate1 = raw.getframerate()
    time1 = numpy.linspace(
        0,
        len(signal1) / f_rate1,
        num=len(signal1)
    )
    # Setting the background color
    ax.set_facecolor("black")
    plt.subplot(2, 1, 1)
    plt.figure(1)
    plt.title("Input Sound Wave")
    plt.xlabel("Time")
    plt.plot(time1, signal1, color='crimson')

    # printing graph of output file using matplotlib.pyplot plt function
    path = final
    raw = wave.open(path)
    signal = raw.readframes(-1)
    signal = numpy.frombuffer(signal, dtype="int16")
    f_rate = raw.getframerate()
    time = numpy.linspace(
        0,
        len(signal) / f_rate,
        num=len(signal)
    )
    # Setting the background color
    ax.set_facecolor("black")
    plt.subplot(2, 1, 2)
    plt.figure(1)
    plt.title("Output Sound Wave")
    plt.xlabel("Time")
    plt.plot(time, signal, color='crimson')
    plt.show()
#changeVolume()
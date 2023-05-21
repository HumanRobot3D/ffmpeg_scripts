#Requirements: installed ffmpeg executable (add to PATH), and ffmpeg-python module.
import ffmpeg
import os

input_file = r"G:\My Drive\WORK\3D_Work\Ants_youtube\renders\map3_trails.mp4"
speed_factor = 5

output_name = os.path.basename(input_file).split(".")[0] + "_" + str(speed_factor) + "x_speed" + ".mp4"
ouput_file = os.path.join(os.path.dirname(input_file),output_name)
stream = ffmpeg.input(input_file)
stream = ffmpeg.output(stream, ouput_file, vf=f"setpts={1/speed_factor}*PTS")
ffmpeg.run(stream)
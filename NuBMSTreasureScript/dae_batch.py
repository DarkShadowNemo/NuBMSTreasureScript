import os
import bpy
# put the location to the folder where the objs are located here in this fashion
# this line will only work on windows ie C:\objects
path_to_obj_dir = os.path.join('C:\\', 'YourPath\\')
# get list of all files in directory
file_list = sorted(os.listdir(path_to_obj_dir))
# get a list of files ending in 'dae'
obj_list = [item for item in file_list if item.endswith('.dae')]
# loop through the strings in obj_list and add the files to the scene
for item in obj_list:
    path_to_file = os.path.join(path_to_obj_dir, item)
    bpy.ops.wm.collada_import(filepath = path_to_file)
    # if heavy importing is expected 
    # you may want use saving to main file after every import
    bpy.ops.wm.save_mainfile(filepath = "C:\\YourPathSavedtoBlend.blend")
import os

folders = os.listdir()

for directory in folders:
    if "." in directory:
        folders.remove(directory)

for folder in folders:
    descriptor = open(f"{folder}/descriptor.mod", "r")
    content = descriptor.readlines()

    for line in content:
        if "name" in line:
            mod_name = line

    mod_name = mod_name.replace('name=','')
    mod_name = mod_name.replace('"','')
    mod_name = mod_name.replace('\n','')

    if ":" in mod_name:
        mod_name = mod_name.replace(':',' - ')
    if "?" in mod_name:
        mod_name = mod_name.replace('?','')

    index_run_location = -1
    for location in content:
        index_run_location += 1
        if "remote_file" in location:
            mod_location = location
            mod_location_index = index_run_location

    index_run_path = -1
    is_Path = False
    for path in content:
        index_run_path += 1
        if "path=" in path:
            mod_path_index = index_run_path
            is_Path = True

    if is_Path == True:
        content[mod_path_index] = f'path="mod/{mod_name}"'
    else:
        content[mod_location_index] = f'path="mod/{mod_name}"'

    new_descriptor = open(f"{mod_name}.mod", "x")
    new_descriptor.write(''.join(content))

    descriptor.close()
    new_descriptor.close()

    descriptor_dir = folder + "/descriptor.mod"
    os.remove(descriptor_dir)
    os.rename(folder, mod_name)

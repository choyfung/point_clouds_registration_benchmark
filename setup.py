import os, shutil
import eth_setup, kaist_setup, planetary_setup, tum_setup

dirname = os.path.abspath(os.path.dirname(__file__))
pairs_dir = os.path.join(dirname, "devel", "registration_pairs")

os.mkdir("eth")
os.chdir("eth")
eth_setup.main()
shutil.copy2(os.path.join(pairs_dir, "apartment_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "apartment_local.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "stairs_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "stairs_local.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "plain_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "plain_local.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "hauptgebaude_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "hauptgebaude_local.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "gazebo_summer_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "gazebo_summer_local.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "gazebo_winter_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "gazebo_winter_local.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "wood_summer_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "wood_summer_local.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "wood_autumn_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "wood_autumn_local.txt"), ".")

os.chdir("..")
os.mkdir("kaist")
os.chdir("kaist")
kaist_setup.main()
shutil.copy2(os.path.join(pairs_dir, "urban05_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "urban05_local.txt"), ".")

os.chdir("..")
os.mkdir("planetary")
os.chdir("planetary")
planetary_setup.main()
shutil.copy2(os.path.join(pairs_dir, "box_met_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "box_met_local.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "p2at_met_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "p2at_met_local.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "planetary_map_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "planetary_map_local.txt"), ".")

os.chdir("..")
os.mkdir("tum")
os.chdir("tum")
tum_setup.main()
shutil.copy2(os.path.join(pairs_dir, "desk_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "desk_local.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "pioneer_slam_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "pioneer_slam_local.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "pioneer_slam2_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "pioneer_slam2_local.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "pioneer_slam3_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "pioneer_slam3_local.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "long_office_household_global.txt"), ".")
shutil.copy2(os.path.join(pairs_dir, "long_office_household_local.txt"), ".")
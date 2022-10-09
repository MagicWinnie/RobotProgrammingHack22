set_do("grab",False)
joint_ptp("home",100.0,100.0,0.0)
### GET TUBE ###
joint_ptp("tube_1_up",100.0,100.0,0.0)
cart_ptp("tube_1_down",100.0,100.0,0.0,"Flange")
set_do("grab",True)
line("tube_1_up_xyz",200.0,1000.0,0.0,"Flange")
### POUR TUBE 1 ###
joint_ptp("ver2_1", 100.0, 100.0, 4)
joint_ptp("ver2_2", 100.0, 100.0, 4)
joint_ptp("ver2_3", 100.0, 100.0, 4)
wait_msec(200)
joint_ptp("ver2_2", 100.0, 100.0, 4)
### PUT TUBE 1 ###
joint_ptp("tube_1_up",100.0,100.0,0.0)
line("tube_1_down",200.0,1000.0,0.0,"Flange")
set_do("grab",False)
cart_ptp("tube_1_up_xyz",100.0,100.0,0.0,"Flange")
### GET TUBE 2 ###
joint_ptp("tube_2_up", 100.0, 100.0, 0.0)
cart_ptp("tube_2_down", 100.0, 100.0, 0.0, "Flange")
set_do("grab",True)
line("tube_2_up_xyz",200.0,1000.0,0.0,"Flange")
### POUR TUBE 2 ###
joint_ptp("ver2_1", 100.0, 100.0, 4)
joint_ptp("ver2_2", 100.0, 100.0, 4)
joint_ptp("ver2_3", 100.0, 100.0, 4)
wait_msec(200)
joint_ptp("ver2_2", 100.0, 100.0, 4)
### PUT TUBE 2 ###
joint_ptp("tube_2_up", 100.0, 100.0, 0.0)
line("tube_2_down",200.0,1000.0,0.0,"Flange")
set_do("grab",False)
cart_ptp("tube_2_up_xyz", 100.0, 100.0, 0.0, "Flange")
### GET BOTTLE ###
joint_ptp("bottle_up",100.0,100.0,0.0)
cart_ptp("bottle_down",100.0,100.0,0.0,"Flange")
set_do("grab",True)
cart_ptp("bottle_up_xyz", 100.0, 100.0, 15, "Flange")
### MIX BOTTLE ###
joint_ptp("bottle_rotate_1", 100.0, 100.0, 10)
for _ in range(5):
    joint_ptp("bottle_rotate_2", 100.0, 100.0, 10)
    joint_ptp("bottle_rotate_3", 100.0, 100.0, 10)
    joint_ptp("bottle_rotate_4", 100.0, 100.0, 10)
    joint_ptp("bottle_rotate_1", 100.0, 100.0, 10)
### PUT BOTTLE ###
joint_ptp("bottle_up", 100.0, 100.0, 15)
cart_ptp("bottle_down",100.0,100.0,0.0,"Flange")
set_do("grab",False)
cart_ptp("bottle_up_xyz", 100.0, 100.0, 10, "Flange")
joint_ptp("home", 100.0, 100.0, 15)

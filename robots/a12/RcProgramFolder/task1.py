set_do("grab",False)
joint_ptp("home",100.0,100.0,0.0)
# TUBE 1
joint_ptp("tube_1_up",100.0,100.0,0.0)
cart_ptp("tube_1_down",100.0,100.0,0.0,"Flange")
set_do("grab",True)
cart_ptp("tube_1_up_xyz",100.0,100.0,0.0,"Flange")
joint_ptp("pour_pt_4", 80, 100.0, 4)
joint_ptp("pour_pt_3", 100.0, 100.0, 4)
joint_ptp("pour_pt_2", 100.0, 100.0, 4)
joint_ptp("pour_pt_1", 100.0, 100.0, 4)
wait_msec(500)
joint_ptp("pour_pt_2", 100.0, 100.0, 4)
joint_ptp("pour_pt_3", 100.0, 100.0, 4)
joint_ptp("pour_pt_4", 100.0, 100.0, 4)
joint_ptp("tube_1_up",100.0,100.0,0.0)
cart_ptp("tube_1_down",100.0,100.0,0.0,"Flange")
set_do("grab",False)
cart_ptp("tube_1_up_xyz",100.0,100.0,0.0,"Flange")
# TUBE 2
joint_ptp("tube_2_up", 100.0, 100.0, 0.0)
cart_ptp("tube_2_down", 100.0, 100.0, 0.0, "Flange")
set_do("grab",True)
cart_ptp("tube_2_up_xyz", 100.0, 100.0, 0.0, "Flange")
joint_ptp("pour_pt_4", 80, 100.0, 4)
joint_ptp("pour_pt_3", 100.0, 100.0, 4)
joint_ptp("pour_pt_2", 100.0, 100.0, 4)
joint_ptp("pour_pt_1", 100.0, 100.0, 4)
wait_msec(500)
joint_ptp("pour_pt_2", 100.0, 100.0, 4)
joint_ptp("pour_pt_3", 100.0, 100.0, 4)
joint_ptp("pour_pt_4", 100.0, 100.0, 4)
joint_ptp("tube_2_up", 100.0, 100.0, 0.0)
cart_ptp("tube_2_down", 100.0, 100.0, 0.0, "Flange")
set_do("grab",False)
cart_ptp("tube_2_up_xyz", 100.0, 100.0, 0.0, "Flange")
# BOTTLE
joint_ptp("bottle_up",100.0,100.0,0.0)
cart_ptp("bottle_down",100.0,100.0,0.0,"Flange")
set_do("grab",True)
cart_ptp("bottle_up_xyz", 100.0, 100.0, 15, "Flange")
# ROTATION OF BOTTLE
for _ in range(5):
    joint_ptp("bottle_rotate_1", 100.0, 100.0, 10)
    joint_ptp("bottle_rotate_2", 100.0, 100.0, 10)
    joint_ptp("bottle_rotate_3", 100.0, 100.0, 10)
    joint_ptp("bottle_rotate_4", 100.0, 100.0, 10)
    joint_ptp("bottle_rotate_1", 100.0, 100.0, 10)
joint_ptp("bottle_up", 100.0, 100.0, 15)
cart_ptp("bottle_down",100.0,100.0,0.0,"Flange")
set_do("grab",False)
cart_ptp("bottle_up_xyz",100.0,100.0,0.0,"Flange")
joint_ptp("home", 100.0, 100.0, 15)

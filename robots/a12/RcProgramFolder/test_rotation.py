joint_ptp("home",100.0,100.0,0.0)
for _ in range(5):
    joint_ptp("bottle_rotate_1", 100.0, 100.0, 5)
    joint_ptp("bottle_rotate_2", 100.0, 100.0, 5)
    joint_ptp("bottle_rotate_3", 100.0, 100.0, 5)
    joint_ptp("bottle_rotate_4", 100.0, 100.0, 5)
    joint_ptp("bottle_rotate_1", 100.0, 100.0, 5)
joint_ptp("home",100.0,100.0,0.0)

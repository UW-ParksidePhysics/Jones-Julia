import vpython as vp

animation_time_step = 0.1  # seconds
rate_of_animation = 1/animation_time_step
time_step = 0.05
stop_time = 10.

initial_position1 = vp.vector(-5, 0., 0.)
initial_velocity1 = vp.vector(1., 0., 0.)
ball1 = vp.sphere(pos=initial_position1, radius=0.1, color=vp.color.red, make_trail=True, trail_type="points", trail_radius=0.1)

initial_position2 = vp.vector(0., -5., 0.)
initial_velocity2 = vp.vector(0., 1., 0.)
ball2 = vp.sphere(pos=initial_position2, radius=0.1, color=vp.color.cyan, make_trail=True, trail_type="points", trail_radius=0.1)

time = 0.
while time < stop_time:
    vp.rate(rate_of_animation)
    x = initial_position1.x + initial_velocity1.x * time
    y = initial_position1.y + initial_velocity1.y * time
    z = initial_position1.z + initial_velocity1.z * time
    ball1.pos = vp.vector(x, y, z)
    x = initial_position2.x + initial_velocity2.x * time
    y = initial_position2.y + initial_velocity2.y * time
    z = initial_position2.z + initial_velocity2.z * time
    ball2.pos = vp.vector(x, y, z)
    time += time_step




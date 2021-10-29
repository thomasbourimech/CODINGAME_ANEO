import sys

def debug(str, params):
    print(str % params, file=sys.stderr, flush=True)

def compute_seconds_to_light(speed, distance):
    return distance / speed

def change_light_state(state):
    if state == "G":
        return "R"
    else:
        return "G"

def compute_distance(v, t):
    return v * t

def compute_state_at_time(t_target, light_duration, state):

    t = 0
    while not t > t_target:
        left = t % light_duration
        if left == 0 and t != 0:
            state = change_light_state(state)
        if t == t_target:
            return state
        t += 0.01
        t = round(t, 2)

    return state


def get_state_at_car_arrival(light_duration, speed, light_distance):

    speed_ms = speed * 1000 / 3600
    time_to_light_no_optim = compute_seconds_to_light(speed_ms, light_distance)
    nb_state_switch = (time_to_light_no_optim // light_duration)

    if (nb_state_switch % 2) == 0:
        state = "G"
    else:
        state = "R"

    time_to_light = round(time_to_light_no_optim % light_duration,2)
    state = compute_state_at_time(time_to_light, light_duration, state)

    return state


init_speed = int(input())
light_count = int(input())
speed = init_speed
tab_state_at_crossing={}
tab_lights = {}

for i in range(light_count):
    light_distance, light_duration = [int(j) for j in input().split()]
    tab_lights[i] = {}
    tab_lights[i]["light_distance"] = light_distance
    tab_lights[i]["light_duration"] = light_duration
    tab_state_at_crossing[i] = "R"

for speed in reversed(range(1, speed + 1)):
    if "R" in tab_state_at_crossing.values():
        for i in range(light_count):
            state = get_state_at_car_arrival(tab_lights[i]["light_duration"], speed, tab_lights[i]["light_distance"])
            if state == "R":
                break
            tab_state_at_crossing[i] = state
    else:
        break
    last_speed = speed
print(last_speed)
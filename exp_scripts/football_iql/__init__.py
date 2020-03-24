import copy

def extend_param_dicts(param_dicts, shared_params, exp_params, repeats=1):
    # copy
    result = copy.deepcopy(shared_params)
    # add experiment parameters to shared params
    result.update(exp_params)
    for i in range(repeats):
        # result.update({"par_id": [i]})
        param_dicts.append(copy.deepcopy(result))
    return param_dicts

server_list = [("gimli", [0,6,7], 6)]

label = "gfootball_iql"
config = "iql"
env_config = "gfootball"

n_repeat = 5

param_dicts = []

shared_params = {
    "t_max": 2000000,
    "epsilon_anneal_time": 250000,
    "buffer_size": 5000,
}


for map_name in ["academy_pass_and_shoot_with_keeper",
                 "academy_run_pass_and_shoot_with_keeper", 
                 "academy_3_vs_1_with_keeper",
                 "academy_counterattack_easy"]:
    extend_param_dicts(param_dicts, shared_params,
        {
            "name": "iql__{}".format(map_name),
            "env_args.map_name": map_name
        },
        repeats=4)

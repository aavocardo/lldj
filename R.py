import rpy2.robjects as r_objects


r_mean = r_objects.r['mean']

demo_list = [5, 10, 15, 20, 35]

r_demo_list = r_objects.IntVector(demo_list)

mean = r_mean(r_demo_list)[0]

print(mean)

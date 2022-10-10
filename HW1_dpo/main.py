import random
import time as time_lib
# Sorry, there are no comments yet


def create_list(lenght, max_value):
    list_tmp = []
    for i in range(lenght):
        list_tmp.append(random.randrange(0, max_value))
    return list_tmp


def calc_hist(input_list):
    hist = [0]*10
    for num in input_list:
        if num < 100:
            hist[0] += 1
        elif num < 200:
            hist[1] += 1
        elif num < 300:
            hist[2] += 1
        elif num < 400:
            hist[3] += 1
        elif num < 500:
            hist[4] += 1
        elif num < 600:
            hist[5] += 1
        elif num < 700:
            hist[6] += 1
        elif num < 800:
            hist[7] += 1
        elif num < 900:
            hist[8] += 1
        elif num < 1000:
            hist[9] += 1
    return hist


# -----Main function-----
def check_time():
    lenght = 1000000
    max_value = 999
    time_dataset = []
    min_time = 10
    max_time = 0
    time = 0
    for i in range(100):
        start_time = time_lib.perf_counter()
        list_tmp = create_list(lenght, max_value)
        calc_hist(list_tmp)
        end_time = time_lib.perf_counter()
        time_required = end_time - start_time
        time_dataset.append(time_required)
        if time_required < min_time:
            min_time = time_required
        if time_required > max_time:
            max_time = time_required
        time += time_required
        print(i)
    time_average = time/100
    print(f"Min time is: {min_time}, max time is: {max_time}, average time is: {time_average}")


# ------Run the program------
if __name__ == "__main__":
    check_time()

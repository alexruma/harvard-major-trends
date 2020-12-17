import matplotlib.pyplot as plt


def plot_graph(concentration_obj):
    """Takes a Concentration object as argument and plots line graph of enrollment history."""

    year_list = []
    enrollment_list = []

    for key in concentration_obj.enrollment_data:
        year_list.append(key)
        enrollment_list.append(concentration_obj.enrollment_data[key])

    plt.plot(year_list, enrollment_list)
    plt.suptitle('Students enrolled in ' + concentration_obj.name)
    plt.show()


import matplotlib.pyplot as plt


def plot_graph(concentration_obj):
    """Takes a Concentration object as argument and plots line graph of enrollment history."""

    year_list = concentration_obj.year_list
    enrollment_list = concentration_obj.enrollment_list

    plt.plot(year_list, enrollment_list)
    plt.suptitle('Students enrolled in ' + concentration_obj.name)
    plt.show()


"""
def plot_multiple(obj1, obj2, obj3):
    plt.subplot(3, 1, 1)
    plt.plot(obj1.year_list, obj1.enrollment_list)
    plt.xlabel('Students enrolled in ' + obj1.name)
    plt.wspace = 0.2  # the amount of width reserved for space between subplots,
    # expressed as a fraction of the average axis width
    plt.hspace = 0.4  # the amount of height reserved for space between subplots,
    # expressed as a fraction of the average axis height

    plt.subplot(3, 1, 2)
    plt.plot(obj2.year_list, obj2.enrollment_list)
    plt.xlabel('Students enrolled in ' + obj2.name)
    plt.hspace = 0.4

    plt.subplot(3, 1, 3)
    plt.plot(obj3.year_list, obj3.enrollment_list)
    plt.xlabel('Students enrolled in ' + obj3.name)
    plt.hspace = 0.4

    plt.show()

"""

def plot_multiple(*concentrations):
    plt.style.use('fivethirtyeight')
    print(plt.style.available)

    for concentration in concentrations:
        plt.plot(concentration.year_list, concentration.enrollment_list, label=concentration.name, marker=".")

    plt.legend()
    #plt.grid(True)
    plt.tight_layout()
    plt.show()

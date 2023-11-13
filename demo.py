import matplotlib.pyplot as plt

from random_hypersphere_hyperball import random_sphere, random_ball


def demo_2d_sphere():
    title = "demo_2d_sphere"

    n = 2000

    x, y = random_sphere(
        number_points=n,
        dimension=2,
    ).T

    color = range(n)

    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, c=color, alpha=0.5, marker="o")
    plt.xlim(-1.2, 1.2)
    plt.ylim(-1.2, 1.2)
    plt.title(title)
    # plt.savefig(title + ".jpg")
    plt.show()


def demo_2d_ball():
    title = "demo_2d_ball"

    n = 2000

    x, y = random_ball(
        number_points=n,
        dimension=2,
    ).T

    color = range(n)

    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, c=color, alpha=0.5, marker="o")
    plt.xlim(-1.2, 1.2)
    plt.ylim(-1.2, 1.2)
    plt.title(title)
    # plt.savefig(title + ".jpg")
    plt.show()


def demo_3d_sphere():
    title = "demo_3d_sphere"

    n = 2000

    x, y, z = random_sphere(
        number_points=n,
        dimension=3,
    ).T

    color = range(n)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=color, alpha=0.5, marker="o")
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_zlim(-1.2, 1.2)
    plt.title(title)
    # plt.savefig(title + ".jpg")
    plt.show()


def demo_3d_ball():
    title = "demo_3d_ball"

    n = 2000

    x, y, z = random_ball(
        number_points=n,
        dimension=3,
    ).T

    color = range(n)

    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(x, y, z, c=color, alpha=0.5, marker="o")
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_zlim(-1.2, 1.2)
    plt.title(title)
    # plt.savefig(title + ".jpg")
    plt.show()


def main():
    demo_2d_sphere()
    demo_2d_ball()
    demo_3d_sphere()
    demo_3d_ball()


if __name__ == "__main__":
    main()

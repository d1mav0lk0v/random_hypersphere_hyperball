"""Random point on a sphere, in a ball.

Uses the numpy package to randomly generate a point.
"""


from numpy import ndarray as __np_array
from numpy.random import random as __rand
from numpy.random import normal as __rand_gauss
from numpy.linalg import norm as __norm_euclid


def random_sphere(
        number_points: int,
        dimension: int = 2,
        radius: __np_array[float] | float = 1,
        center: __np_array[float] | float = 0,
    ) -> __np_array[__np_array[float]]:
    """Return random points on the sphere.

    Args:
        number_points (int): Number of points on the sphere. Positive integer.
        dimension (int): Dimension of the hypersphere. Positive integer.
            Defaults to 2.
        radius (__np_array[float] | float): Radius of the sphere, array of
            semi-axes (the number must be equal to dimension). Defaults to 1.
        center (__np_array[float] | float): Center of the sphere, array of
            coords (the number must be equal to dimension). Defaults to 0.

    Returns:
        __np_array[__np_array[float]]: Array of points, 
            shape=(number_points, dimension).
    """

    coords = __rand_gauss(size=(number_points, dimension))
    coords /= __norm_euclid(coords, axis=1, keepdims=True)
    coords *= radius
    coords += center

    return coords


def random_ball(
        number_points: int,
        dimension: int = 2,
        radius: __np_array[float] | float = 1,
        center: __np_array[float] | float = 0,
    ) -> __np_array[__np_array[float]]:
    """Return random points in the ball.

    Args:
        number_points (int): Number of points in the sphere. Positive integer.
        dimension (int): Dimension of the hyperball. Positive integer.
            Defaults to 2.
        radius (__np_array[float] | float): Radius of the ball, array of
            semi-axes (the number must be equal to dimension). Defaults to 1.
        center (__np_array[float] | float): Center of the ball, array of
            coords (the number must be equal to dimension). Defaults to 0.

    Returns:
        __np_array[__np_array[float]]: Array of points, 
            shape=(number_points, dimension).
    """
    
    coords = random_sphere(
        number_points=number_points,
        dimension=dimension,
        radius=1,
        center=0,
    )

    coords *= __rand((number_points, 1)) ** (1 / dimension)
    coords *= radius
    coords += center

    return coords

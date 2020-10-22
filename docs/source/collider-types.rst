Colliders
=========

The library provides two different collider types convex and concaves.
Both supported types requires knowledge that you use the correct type of
collider. Colliders themselves don't yet provide validation.

Usage
-----

.. versionchanged:: 0.1.4

Easiest way to create colliders is to import ``create_collider`` function and
use that to create colliders:

.. code-block:: python

    from pygame_colliders import create_collider

    convex_poly_points = [(13, 10), (13, 3), (6, 3), (6, 10)]
    convex_collider = create_collider(convex_poly_points)

    concave_poly_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]
    concave_collider = create_collider(collider_points)

Using the colliders is easy. Just create a collider like instructed above and
then test if two colliders do collide against each other:

.. code-block:: python

    collider_a_points = [(13, 10), (13, 3), (6, 3), (6, 10)]
    collider_a = create_collider(collider_points)

    collider_b_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]
    collider_b = create_collider(collider_points)

    if collider_a.collide(collider_b):
        print("Collision detected")

Convex colliders
----------------

Convex colliders are the simpler ones of the two supported. In convex collider
all inner angles are less or equal to 180 degrees.

Creating a convex collider:

.. code-block:: python

    collider_points = [(13, 10), (13, 3), (6, 3), (6, 10)]
    collider = ConvexCollider(collider_points)

.. seealso::
    Math Open Reference provides `interactive tool <https://www.mathopenref.com/polygonconvex.html>`_
    to try out convex polygons.

Concave colliders
-----------------

In concave colliders one or more inner angles are greater than 180. All
convex colliders are concave polygons as well.

Using the concave collider causes in the initial stage splitting the concave
collider to a convex colliders.

Creating a concave collider:

.. code-block:: python

    collider_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]
    collider = ConcaveCollider(collider_points)

The code above creates C-shaped collider.

.. seealso::
    Math Open Reference provides `interactive tool <https://www.mathopenref.com/polygonconcave.html>`_
    to try out concave polygons.

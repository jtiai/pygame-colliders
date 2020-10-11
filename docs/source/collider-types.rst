Colliders
=========

The library provides two different collider types convex and concaves.
Both supported types requires knowledge that you use the correct type of
collider. Colliders themselves don't yet provide validation.

Convex colliders
----------------

Convex colliders are the simpler ones of the two supported. In convex collider
all inner angles are less or equal to 180 degrees.

Creating a convex collider:

.. code-block:: python

    poly_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]
    collider = ConcaveCollider(poly_points)

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

    poly_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]
    collider = ConcaveCollider(poly_points)

The code above creates C-shaped collider.

.. seealso::
    Math Open Reference provides `interactive tool <https://www.mathopenref.com/polygonconcave.html>`_
    to try out concave polygons.

Using colliders
---------------

Using the colliders is easy. Just create a collider like instructed above and
then test if two colliders do collide against each other:

.. code-block:: python

    if collider_a.collide(collider_b):
        print("Collision detected")

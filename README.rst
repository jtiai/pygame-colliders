Pygame Colliders
================

Pygame colliders will enhance your game or application to have more complex
colliding system beyond standard ``Rect`` colliders in Pygame.

Despite the name colliders aren't bound to Pygame and Pygame library is not
prerequisite.

Usage
-----

Look how easy it is to use:

.. code-block:: python

    from pygame_colliders import ConcaveCollider, ConvexCollider

    # Create colliders
    collider_a_points = [(3, 3), (5, 3), (5, 4), (4, 4), (4, 5), (5, 5), (5, 6), (3, 6)]
    collider_b_points = [(4.5, 3.5), (6, 2), (6, 4)]

    collider_a = ConcaveCollider(poly_a_points)
    collider_b = ConvexCollider(poly_b_points)

    # Check collision
    if collider_a.collide(collider_b):
        print("Collision detected!")

Features
--------

Collisions between

Installation
------------

Install pygame colliders by running:

    pip install pygame-colliders

Contribute
----------

- Issue Tracker: github.com/jtiai/pygame-colliders/issues
- Source Code: github.com/jtiai/pygame-colliders

Support
-------

If you are having issues, please let us know.
We have a Discord channel located at : https://discord.gg/VXVRPxe

License
-------

The project is licensed under the 3-clause BSD license.

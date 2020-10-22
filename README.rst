Pygame Colliders
================

.. image:: https://readthedocs.org/projects/pygame-colliders/badge/?version=latest
    :target: https://pygame-colliders.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://github.com/jtiai/pygame-colliders/workflows/Test%20and%20lint/badge.svg
    :alt: Test and lint

.. image:: https://github.com/jtiai/pygame-colliders/workflows/Build%20and%20publish%20packages/badge.svg
    :alt: Build and publish packages

Pygame colliders will enhance your game or application to have more complex
colliding system beyond standard ``Rect`` colliders in Pygame.

Despite the name colliders aren't bound to Pygame and Pygame library is not
prerequisite.

Documentation
-------------

Documentation is located at https://pygame-colliders.readthedocs.io/

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

- Issue Tracker: https://github.com/jtiai/pygame-colliders/issues
- Source Code: https://github.com/jtiai/pygame-colliders

Support
-------

If you are having issues, please let us know.
We have a Discord channel located at : https://discord.gg/VXVRPxe

License
-------

The project is licensed under the 3-clause BSD license.

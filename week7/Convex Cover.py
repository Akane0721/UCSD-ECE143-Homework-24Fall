import numpy as np


def find_convex_cover(pvertices, clist):
    """
    compute the radii of m circles centered at m points such that the sum of the areas of the circles is minimized (approximately)
    and that any vertex in P is also contained in at least one of the m circles.

    Args:
        pvertices (np.ndarray): coordinates of vertices
        clist (list):coordinates of centers
    """
    assert isinstance(pvertices, np.ndarray) and isinstance(clist, list)
    clist = np.array(clist)

    r = np.zeros(len(clist))
    mask = np.ones(len(pvertices), dtype=bool)

    while np.sum(mask):
        distances = np.linalg.norm(pvertices[mask, None, :] - clist[None, :, :], axis=2)
        min_distances = np.min(distances, axis=1)
        closest_centers = np.argmin(distances, axis=1)
        best_vertex_index = np.argmax(min_distances)
        best_center_index = closest_centers[best_vertex_index]

        r[best_center_index] = max(
            r[best_center_index], min_distances[best_vertex_index]
        )

        uncovered_indices = np.where(mask)[0]
        mask[uncovered_indices[best_vertex_index]] = False

    return r


"""
pvertices = np.array(
    [
        [0.573, 0.797],
        [0.688, 0.402],
        [0.747, 0.238],
        [0.802, 0.426],
        [0.757, 0.796],
        [0.589, 0.811],
    ]
)

clist = [
    (0.7490863467660889, 0.4917635308023209),
    (0.6814339441396109, 0.6199470305156477),
    (0.7241617773773865, 0.6982813914515696),
    (0.6600700275207232, 0.7516911829987891),
    (0.6315848053622062, 0.7730550996176769),
    (0.7348437356868305, 0.41342916986639894),
    (0.7597683050755328, 0.31729154508140384),
]
print(find_convex_cover(pvertices, clist))
"""

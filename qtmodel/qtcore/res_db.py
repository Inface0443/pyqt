class BeamForce:
    def __init__(self, beam_id, force_i, force_j):
        if isinstance(beam_id, int) and len(force_i) == 6 and len(force_j) == 6:
            self.id = beam_id
            self.force_i = list(force_i)
            self.force_j = list(force_j)
        else:
            raise ValueError("Invalid input: 'id' must be an integer, and 'force_i' and 'force_j' must be lists of length 6.")

    def __str__(self):
        return f"BeamId:{self.id}\nForceI: {self.force_i}\nForceJ: {self.force_j}"


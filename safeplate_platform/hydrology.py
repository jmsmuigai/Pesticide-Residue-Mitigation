"""
SCS-CN Hydrological Pesticide Runoff Modeling Module
Calculates surface runoff depth (Q in mm) based on precipitation (P in mm)
and land-cover Curve Number (CN).
Formula:
  S = (25400 / CN) - 254
  Ia = 0.2 * S
  If P > Ia: Q = ((P - Ia) ** 2) / (P - Ia + S)
  Else: Q = 0.0
"""

class HydrologyModel:
    def __init__(self, default_cn: float = 79.0):
        self.default_cn = default_cn

    def calculate_runoff(self, precipitation: float, curve_number: float = None) -> float:
        """
        Calculates surface runoff Q (mm) given precipitation P (mm) and Curve Number CN.
        Returns Q rounded to 2 decimal places (or float value).
        """
        cn = curve_number if curve_number is not None else self.default_cn
        if cn <= 0 or cn > 100:
            raise ValueError("Curve Number must be between 0 and 100.")
        
        S = (25400.0 / cn) - 254.0
        Ia = 0.2 * S
        
        if precipitation <= Ia:
            return 0.0
        
        numerator = (precipitation - Ia) ** 2
        denominator = (precipitation - Ia) + S
        Q = numerator / denominator
        return round(Q, 4)

def calculate_runoff(precipitation: float, curve_number: float = 79.0) -> float:
    model = HydrologyModel(default_cn=curve_number)
    return model.calculate_runoff(precipitation=precipitation, curve_number=curve_number)

def self_test():
    """
    Runs self-test: Q(P=55, CN=79) must equal 15.80 mm
    """
    P = 55.0
    CN = 79.0
    q_val = calculate_runoff(P, CN)
    q_rounded = round(q_val, 2)
    assert abs(q_rounded - 15.80) < 0.01, f"Self-test failed: Q({P}, {CN}) = {q_val} != 15.80"
    return {
        "status": "PASSED",
        "P_mm": P,
        "CN": CN,
        "Q_mm": q_val,
        "Q_formatted": f"{q_rounded:.2f} mm"
    }

if __name__ == "__main__":
    result = self_test()
    print(f"Hydrology Self-Test Output: {result}")

import numpy as np

class McCabeThiele:
    def __init__(self, vle_x, vle_y):
        # Fit a polynomial to VLE data for easier calculation
        # Order 5 captures the Ethanol-Water azeotrope reasonably well
        self.vle_poly = np.poly1d(np.polyfit(vle_x, vle_y, 5))
        
    def get_y_eq(self, x):
        """Equilibrium vapor fraction for a given liquid fraction x"""
        return np.clip(self.vle_poly(x), 0, 1)

    def rect_line(self, x, R, xd):
        """Rectification operating line"""
        return (R / (R + 1)) * x + (xd / (R + 1))

    def q_line(self, x, xf, q):
        """Feed (q) line"""
        if q == 1: # Saturated liquid (vertical line)
            return None 
        return (q / (q - 1)) * x - (xf / (q - 1))

    def calculate_stages(self, xf, xd, xw, R, q):
        """
        Calculates theoretical stages stepping from xd down to xw.
        Returns a list of points (x, y) for the staircase plot.
        """
        stages = []
        curr_x = xd
        curr_y = xd
        
        # Point on diagonal (xd, xd)
        stages.append((curr_x, curr_y))
        
        # Calculate intersection of rect line and q-line
        # For simplicity, if q is vertical, x_int = xf
        if abs(q - 1) < 1e-3:
            x_int = xf
        else:
            # (R/(R+1))x + xd/(R+1) = (q/(q-1))x - xf/(q-1)
            m1 = R / (R + 1)
            c1 = xd / (R + 1)
            m2 = q / (q - 1)
            c2 = -xf / (q - 1)
            x_int = (c2 - c1) / (m1 - m2)
        
        limit = 50 # Safeguard
        while curr_x > xw and limit > 0:
            # Horizontal step to equilibrium curve
            # y remains same, x is found by solving vle_poly(x) = y
            # For simplicity in this demo, we can use a small search or just invert the poly
            # Here I'll use a simple root finder or interpolation
            # Since vle is monotonic, we can interpolate
            target_y = curr_y
            # Simplified: search for x such that vle_poly(x) approx y
            test_x = np.linspace(0, 1, 1000)
            test_y = self.get_y_eq(test_x)
            curr_x = np.interp(target_y, test_y, test_x)
            stages.append((curr_x, curr_y))
            
            if curr_x <= xw:
                break
                
            # Vertical step to operating line
            if curr_x > x_int:
                # Still in rectification section
                curr_y = self.rect_line(curr_x, R, xd)
            else:
                # In stripping section
                # Line from (x_int, y_int) to (xw, xw)
                y_int = self.rect_line(x_int, R, xd)
                m_strip = (y_int - xw) / (x_int - xw)
                c_strip = xw - m_strip * xw
                curr_y = m_strip * curr_x + c_strip
                
            stages.append((curr_x, curr_y))
            limit -= 1
            
        return stages


def poly_add2(p1, p2):
   p3 = []  
   p3.append(p1[0]+p2[0])
   p3.append(p1[1]+p2[1])
   p3.append(p1[2]+p2[2])
   return p3

def poly_mult2(p1, p2):
   p3 = [0,0,0,0,0]

   p3[0] += (p1[0]*p2[0])
   p3[1] += (p1[0]*p2[1])
   p3[2] += (p1[0]*p2[2])
   p3[1] += (p1[1]*p2[0])
   p3[2] += (p1[1]*p2[1])
   p3[3] += (p1[1]*p2[2])
   p3[2] += (p1[2]*p2[0])
   p3[3] += (p1[2]*p2[1])
   p3[4] += (p1[2]*p2[2])
   return p3


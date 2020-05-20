import vectors

class Brain:
    def __init__(self):
        self.fighters = []

    def control(self,player):
        for i in range(len(self.fighters)):
            fa = self.fighters[i]
            fa.receive_signal(["noslowdown"])
            for j in range(i+1,len(self.fighters)):
                print(i,j)
                fb = self.fighters[j]
                if vectors.norm(vectors.sub_vec(fa.pos,fb.pos)) <450:
                    d1 = vectors.norm(vectors.sub_vec(fa.v,player.pos))
                    d2 = vectors.norm(vectors.sub_vec(fb.v,player.pos))
                    if d1 < d2:
                        #fa is closen
                        # print("Slos")
                        fb.receive_signal(["slowdown"])
                    else:
                        fa.receive_signal(["slowdown"])
                else:
                    fa.receive_signal(["noslowdown"])
                    fb.receive_signal(["noslowdown"])

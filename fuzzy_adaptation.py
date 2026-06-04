shared_brain={
    "aggression":0.5,
    "speed":1.0,
    "attack_range":40
}

def update_brain(pb):
    if not hasattr(pb,"movement_intensity"): return

    if pb.avg_distance_to_npcs>250:
        shared_brain["aggression"]=min(1,shared_brain["aggression"]+0.02)
        shared_brain["speed"]=min(2,shared_brain["speed"]+0.01)

    elif pb.avg_distance_to_npcs<120:
        shared_brain["aggression"]=max(0.2,shared_brain["aggression"]-0.02)
        shared_brain["speed"]=max(0.7,shared_brain["speed"]-0.01)

    if pb.movement_intensity>200:
        shared_brain["attack_range"]=min(80,shared_brain["attack_range"]+1)
    else:
        shared_brain["attack_range"]=max(30,shared_brain["attack_range"]-1)
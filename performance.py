import psutil

class PerformanceTracker:
    def __init__(self):
        self.fps_list=[]; self.cpu_list=[]; self.ram_list=[]

    def update(self,clock):
        fps=clock.get_fps()
        cpu=psutil.cpu_percent()
        ram=psutil.Process().memory_info().rss/(1024*1024)

        if fps>0:
            self.fps_list.append(fps)
            self.cpu_list.append(cpu)
            self.ram_list.append(ram)

    def get_averages(self):
        if not self.fps_list: return 0,0,0
        return sum(self.fps_list)/len(self.fps_list),sum(self.cpu_list)/len(self.cpu_list),sum(self.ram_list)/len(self.ram_list)

    def reset(self):
        self.fps_list.clear(); self.cpu_list.clear(); self.ram_list.clear()
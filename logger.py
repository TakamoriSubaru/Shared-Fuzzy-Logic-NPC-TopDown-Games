import csv,os,config

def init_csv():
    if not os.path.exists(config.CSV_FILE):
        with open(config.CSV_FILE,"w",newline="") as f:
            csv.writer(f).writerow(["Run","Mode","NPC_Count","Survival_Time","Avg_FPS","Avg_CPU","Avg_RAM_MB"])

def log_run(run_number,survival_time,avg_fps,avg_cpu,avg_ram):
    mode="Adaptive" if config.ADAPTIVE_AI else "Baseline"
    with open(config.CSV_FILE,"a",newline="") as f:
        csv.writer(f).writerow([run_number,mode,config.NPC_COUNT,round(survival_time,2),round(avg_fps,2),round(avg_cpu,2),round(avg_ram,2)])
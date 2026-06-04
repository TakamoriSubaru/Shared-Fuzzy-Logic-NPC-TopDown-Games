import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ================= LOAD DATA =================
adaptive = pd.read_csv("results_adaptive.csv")
baseline = pd.read_csv("results_baseline.csv")

print("Adaptive runs:", len(adaptive))
print("Baseline runs:", len(baseline))

surv_ad = adaptive["Survival_Time"]
surv_base = baseline["Survival_Time"]

# =========================================================
# 1️⃣ BOXPLOT (kamu sudah punya tapi kita simpan lagi)
# =========================================================
plt.figure()
plt.boxplot([surv_base, surv_ad], labels=["Baseline AI", "Adaptive AI"])
plt.title("Adaptive AI vs Baseline AI")
plt.ylabel("Survival Time (seconds)")
plt.savefig("boxplot.png")
plt.show()


# =========================================================
# 2️⃣ HISTOGRAM DISTRIBUTION
# =========================================================
plt.figure()
plt.hist(surv_base, bins=20, alpha=0.5, label="Baseline")
plt.hist(surv_ad, bins=20, alpha=0.5, label="Adaptive")
plt.legend()
plt.title("Distribution of Survival Time")
plt.xlabel("Seconds")
plt.ylabel("Frequency")
plt.savefig("histogram.png")
plt.show()


# =========================================================
# 3️⃣ MEAN + STD BAR CHART
# =========================================================
mean_base = np.mean(surv_base)
mean_ad = np.mean(surv_ad)

std_base = np.std(surv_base)
std_ad = np.std(surv_ad)

plt.figure()
plt.bar(["Baseline", "Adaptive"], [mean_base, mean_ad], yerr=[std_base, std_ad])
plt.title("Mean Survival Time Comparison")
plt.ylabel("Seconds")
plt.savefig("mean_bar.png")
plt.show()

print("Mean Baseline:", mean_base)
print("Mean Adaptive:", mean_ad)


# =========================================================
# 4️⃣ SURVIVAL CURVE (SUPER IMPORTANT)
# =========================================================
def survival_curve(data):
    sorted_times = np.sort(data)
    survival_prob = 1.0 - np.arange(len(sorted_times)) / len(sorted_times)
    return sorted_times, survival_prob

t_base, s_base = survival_curve(surv_base)
t_ad, s_ad = survival_curve(surv_ad)

plt.figure()
plt.plot(t_base, s_base, label="Baseline")
plt.plot(t_ad, s_ad, label="Adaptive")
plt.legend()
plt.title("Survival Curve")
plt.xlabel("Time (seconds)")
plt.ylabel("Probability Alive")
plt.savefig("survival_curve.png")
plt.show()


# =========================================================
# 5️⃣ LEARNING TREND (Adaptive only)
# =========================================================
plt.figure()
plt.plot(adaptive["Run"], adaptive["Survival_Time"])
plt.title("Adaptive AI Learning Trend")
plt.xlabel("Run")
plt.ylabel("Survival Time")
plt.savefig("learning_curve.png")
plt.show()

print("All plots saved ✔")
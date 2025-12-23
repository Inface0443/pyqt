import numpy as np
import matplotlib.pyplot as plt
# aaa

def clamp01(x):
    return np.clip(x, 0.0, 1.0)

# =========================
# BetaFitBh1
# =========================
def bh1_beta_rho08(x):
    x = clamp01(x)
    return 1.0 + 0.698873 * np.power(1.0 - x, 2.866872)

def bh1_beta_rho06(x):
    x = clamp01(x)
    return 1.0 + 1.395898 * np.power(1.0 - x, 2.442155)

def bh1_beta_rho05(x):
    x = clamp01(x)
    t = 1.0 - x
    return 1.0 + 1.364765 * np.power(t, 1.508847) + 1.544109 * np.power(t, 3.619435)

def bh1_beta(rho, Af, Aw):
    if not np.isfinite(rho):
        raise ValueError("rho 必须是有限实数")
    if Aw <= 0:
        raise ValueError("Aw 必须 > 0")

    x = clamp01(Af / Aw)

    # 允许超出范围
    if rho <= 0.5:
        return float(bh1_beta_rho05(x))
    if rho >= 0.8:
        return float(bh1_beta_rho08(x))

    if rho <= 0.6:
        b05 = bh1_beta_rho05(x)
        b06 = bh1_beta_rho06(x)
        t = (rho - 0.5) / 0.1
        return float(b05 + t * (b06 - b05))
    else:
        b06 = bh1_beta_rho06(x)
        b08 = bh1_beta_rho08(x)
        t = (rho - 0.6) / 0.2
        return float(b06 + t * (b08 - b06))

# =========================
# BetaFitBh2
# =========================
def bh2_beta_rho04(x):
    x = clamp01(x)
    return 1.352128 + 3.597872 * np.power(1.0 - x, 2.539312)

def bh2_beta_rho06(x):
    x = clamp01(x)
    return 1.352128 + 1.788404 * np.power(1.0 - x, 2.266723)

def bh2_beta_rho08(x):
    x = clamp01(x)
    t = 1.0 - x
    return 1.3 + 0.095 * np.power(t, 0.278608) + 1.0 * np.power(t, 4.832105)

def bh2_beta(rho, Af, Aw):
    if Aw <= 0:
        raise ValueError("Aw 必须 > 0")
    if not np.isfinite(rho):
        raise ValueError("rho 必须是有限实数")

    x = clamp01(Af / Aw)

    # 允许超出范围（按你 C# 的逻辑）
    if rho <= 0.4:
        return float(bh2_beta_rho04(x))
    if rho >= 0.8:
        return float(bh2_beta_rho08(x))

    if rho <= 0.6:
        b04 = bh2_beta_rho04(x)
        b06 = bh2_beta_rho06(x)
        a = (rho - 0.4) / 0.2
        return float(b04 + a * (b06 - b04))
    else:
        b06 = bh2_beta_rho06(x)
        b08 = bh2_beta_rho08(x)
        a = (rho - 0.6) / 0.2
        return float(b06 + a * (b08 - b06))

# =========================
# 绘图（两张图）
# =========================
x = np.linspace(0.0, 1.0, 401)

# 图1：Bh1 的三条曲线
plt.figure()
plt.plot(x, bh1_beta_rho05(x), label="rho=0.5")
plt.plot(x, bh1_beta_rho06(x), label="rho=0.6")
plt.plot(x, bh1_beta_rho08(x), label="rho=0.8")

# 可选：画几条插值 rho 的曲线（想更像“面内插值效果”就打开）
# for r in [0.55, 0.65, 0.70, 0.75]:
#     plt.plot(x, [bh1_beta(r, Af=xi, Aw=1.0) for xi in x], label=f"rho={r:g}", linewidth=1)

plt.xlabel("Af/Aw")
plt.ylabel("β")
plt.title("B/H=1")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

# 图2：Bh2 的三条曲线
plt.figure()
plt.plot(x, bh2_beta_rho04(x), label="rho=0.4")
plt.plot(x, bh2_beta_rho06(x), label="rho=0.6")
plt.plot(x, bh2_beta_rho08(x), label="rho=0.8")

# 可选：插值 rho 曲线
# for r in [0.45, 0.50, 0.55, 0.65, 0.70, 0.75]:
#     plt.plot(x, [bh2_beta(r, Af=xi, Aw=1.0) for xi in x], label=f"rho={r:g}", linewidth=1)

plt.xlabel("Af/Aw")
plt.ylabel("beta")
plt.title("B/H=2")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()

plt.show()

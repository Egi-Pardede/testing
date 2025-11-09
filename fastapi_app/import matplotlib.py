import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# === IRR CHART ===
irr_value = 1.45  # 145%
discount_rate = 0.10  # 10%

axes[0].bar(['IRR'], [irr_value], color='mediumseagreen', width=0.4)
axes[0].axhline(discount_rate, color='orange', linestyle='--', linewidth=2, label='Discount Rate (10%)')
axes[0].set_title('Internal Rate of Return (IRR)')
axes[0].set_ylabel('Rasio')
axes[0].legend()
axes[0].grid(axis='y')

# === PAYBACK PERIOD CHART ===
years = np.array([0, 1, 2, 3])
cumulative = np.array([-80_000_000, -20_000_000, 60_000_000, 140_000_000])
payback_point = 1.77

axes[1].plot(years, cumulative, marker='o', color='mediumseagreen', linewidth=2, label='Arus Kas Kumulatif')
axes[1].axhline(0, color='orange', linestyle='--', linewidth=2, label='Titik Impas (Rp 0)')
axes[1].axvline(payback_point, color='purple', linestyle=':', linewidth=2, label=f'Payback ≈ {payback_point} Tahun')
axes[1].set_title('Payback Period')
axes[1].set_xlabel('Tahun')
axes[1].set_ylabel('Arus Kas Kumulatif (Rp)')
axes[1].legend()
axes[1].grid(axis='both')

plt.tight_layout()
plt.show()

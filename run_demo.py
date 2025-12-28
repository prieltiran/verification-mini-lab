from signal_generator import generate_sine, generate_square, generate_noise
from checks import check_clipping, rms_level

signals = {
    "Sine": generate_sine(),
    "Square": generate_square(),
    "Noise": generate_noise()
}

print("Verification Report")
print("-------------------")

for name, sig in signals.items():
    clipped = check_clipping(sig)
    rms = rms_level(sig)
    print(f"{name}: RMS={rms:.3f}, Clipping={'YES' if clipped else 'NO'}")

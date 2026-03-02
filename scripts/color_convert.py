import sys
try:
    from coloraide import Color
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable,'-m','pip','install','coloraide'])
    from coloraide import Color

c = Color('oklch(39.34% 0.170 279.64)')
print(c.convert('srgb').to_string(hex=True))

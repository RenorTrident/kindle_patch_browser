# Kindle Oasis 3 Facebook Browser Patcher

**A jailbreak-compatible web browser for Kindle Oasis 3 (WiFi, 8GB) that enables Facebook access through Kual.**

## Features
- ✅ Facebook support via mobile/lite version
- ✅ Kual launcher integration
- ✅ Multi-language codebase (Python, C, Shell, JavaScript)
- ✅ Touch-optimized interface for Kindle Oasis 3
- ✅ Cookie/session persistence
- ✅ Hardware button support

## Device Requirements
- **Device**: Kindle Oasis 3 (8GB WiFi)
- **OS**: 5.x-5.14.x
- **Jailbreak**: Kual-enabled
- **Storage**: ~50MB free space

## Project Structure

```
kindle_patch_browser/
├── README.md
├── kual/                          # Kual launcher extension
│   ├── KindleExtensions/
│   │   └── facebook_browser/
│   │       ├── menu.json
│   │       ├── script.sh
│   │       └── assets/
├── python/                        # Python web wrapper
│   ├── main.py
│   ├── browser.py
│   ├── facebook_handler.py
│   ├── config.py
│   └── requirements.txt
├── c/                             # C-based lightweight browser
│   ├── CMakeLists.txt
│   ├── src/
│   │   ├── main.c
│   │   ├── browser.c
│   │   ├── network.c
│   │   └── touch_handler.c
│   └── include/
│       └── browser.h
├── js/                            # JavaScript utilities
│   ├── facebook_shim.js
│   ├── ua_spoofer.js
│   └── inject.js
├── config/                        # Configuration files
│   ├── facebook_urls.conf
│   ├── browser.conf
│   └── certificates/
├── docs/                          # Documentation
│   ├── INSTALLATION.md
│   ├── USAGE.md
│   ├── TROUBLESHOOTING.md
│   └── DEVELOPMENT.md
└── scripts/                       # Utility scripts
    ├── build.sh
    ├── install.sh
    └── test.sh
```

## Quick Start

### 1. Installation
```bash
# Clone the repo
git clone https://github.com/RenorTrident/kindle_patch_browser.git
cd kindle_patch_browser

# Copy to Kindle via USB
cp -r kual/KindleExtensions/facebook_browser /mnt/kindle/extensions/

# Reboot Kindle
```

### 2. Launch from Kual
- Press **Menu** → Select **Facebook Browser** → Press **Select**

### 3. Use
- Navigate with Kindle buttons
- Tap screen for input
- Swipe for scrolling

## Implementation Status

| Component | Status | Language |
|-----------|--------|----------|
| Kual Launcher | ⏳ In Progress | Shell |
| Python Wrapper | ⏳ In Progress | Python |
| C Browser | ⏳ Planned | C |
| JS Injection | ⏳ Planned | JavaScript |
| Config System | ⏳ Planned | YAML/JSON |

## Technical Notes

### Kindle Oasis 3 Specs
- CPU: Freescale i.MX6SL (ARM Cortex-A9 @ 1GHz)
- RAM: 512MB
- Screen: 7" E Ink (1680×1264)
- Touch: Capacitive touch panel
- OS: Linux kernel 3.0.35

### Facebook Compatibility
Uses mobile version:
- `m.facebook.com` (older, lighter)
- `mbasic.facebook.com` (lightest alternative)
- User-Agent spoofing to bypass device restrictions
- Cookie persistence for sessions

## Building from Source

```bash
# Install dependencies
sudo apt-get install build-essential libcurl4-openssl-dev libssl-dev

# Build C component (optional, performance)
cd c/
mkdir build && cd build
cmake ..
make

# Run Python version (primary)
cd ../../python
pip install -r requirements.txt
python main.py
```

## Troubleshooting

See [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) for common issues.

## Legal Notice

This project is for **personal use only** on jailbroken devices. Users are responsible for:
- Complying with Facebook's Terms of Service
- Respecting Amazon's Terms of Service for jailbroken devices
- Any network/data usage charges

## Contributing

Contributions welcome! Please:
1. Fork the repo
2. Create a feature branch (`git checkout -b feature/YourFeature`)
3. Commit changes (`git commit -m 'Add feature'`)
4. Push to branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

## License

MIT License - See LICENSE file for details

## Author

@RenorTrident

## References

- [Kindle Oasis 3 Specs](https://www.amazon.com/Kindle-Oasis-now-adjustable-warm/dp/B07FKR6KXF)
- [MobileRead Forum - Kindle Hacking](https://www.mobileread.com/)
- [Kual Documentation](https://github.com/ixtab/Kual)
- [Facebook Mobile](https://m.facebook.com)

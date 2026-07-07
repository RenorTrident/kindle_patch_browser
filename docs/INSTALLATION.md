# Installation Guide - Kindle Facebook Browser

## Prerequisites

### Device Requirements
- **Device**: Kindle Oasis 3 (8GB WiFi variant)
- **OS Version**: 5.x to 5.14.x
- **Free Storage**: At least 50MB
- **Jailbreak Status**: Must be jailbroken with Kual installed

### Computer Requirements
- USB cable for connecting Kindle
- File manager with USB support
- (Optional) Development tools for building from source

## Step 1: Prepare Your Kindle

### 1.1 Enable Developer Mode
1. Connect your Kindle to USB
2. Enable USB mass storage mode
3. Backup your data (optional but recommended)

### 1.2 Verify Kual Installation
1. Press **Menu** → **Settings** → **Device Info** → **Menu** (again)
2. Select **Update Your Kindle**
3. You should see a Kual menu item

If Kual is not installed, visit [MobileRead - Kual](https://www.mobileread.com/) for installation instructions.

## Step 2: Install Facebook Browser

### 2.1 Via USB (Recommended for Beginners)

1. **Clone/Download the Repository**
   ```bash
   git clone https://github.com/RenorTrident/kindle_patch_browser.git
   cd kindle_patch_browser
   ```

2. **Connect Kindle via USB**
   - Mac/Linux: Automatically mounts as `/Volumes/Kindle` or `/mnt/kindle`
   - Windows: Shows as a drive letter (e.g., `E:\`)

3. **Copy Files to Kindle**
   ```bash
   # Mac/Linux
   cp -r kual/KindleExtensions/facebook_browser /Volumes/Kindle/extensions/
   cp -r python /Volumes/Kindle/extensions/facebook_browser/
   cp -r config /Volumes/Kindle/extensions/facebook_browser/
   
   # Windows (using PowerShell or Command Prompt)
   xcopy kual\KindleExtensions\facebook_browser E:\extensions\ /E /I
   xcopy python E:\extensions\facebook_browser\ /E /I
   xcopy config E:\extensions\facebook_browser\ /E /I
   ```

4. **Disconnect Safely**
   - Press **Menu** → **Disconnect** on Kindle
   - Or eject from your computer

5. **Reboot Kindle**
   - Hold power button for 15+ seconds
   - Release when powered off
   - Press power button again to turn on

### 2.2 Via SSH (For Advanced Users)

1. **Enable SSH on Kindle**
   ```bash
   # If already jailbroken, SSH might be enabled
   # Check by trying to connect
   ssh root@192.168.1.X  # Replace X with your Kindle's IP
   ```

2. **Transfer Files via SCP**
   ```bash
   scp -r kual/KindleExtensions/facebook_browser root@192.168.1.X:/mnt/us/extensions/
   scp -r python root@192.168.1.X:/mnt/us/extensions/facebook_browser/
   scp -r config root@192.168.1.X:/mnt/us/extensions/facebook_browser/
   ```

3. **Set Permissions**
   ```bash
   ssh root@192.168.1.X "chmod -R 755 /mnt/us/extensions/facebook_browser"
   ```

## Step 3: Verify Installation

1. **Check Kual Menu**
   - Press **Menu** → Should see **Facebook Browser** option

2. **Launch Application**
   - Select **Facebook Browser** from Kual
   - Press **Select**
   - Browser should start loading

3. **Check Logs** (if issues occur)
   ```bash
   # Via SSH
   ssh root@192.168.1.X
   tail -f /var/log/facebook_browser.log
   ```

## Step 4: Initial Setup

### 4.1 First Launch
1. Browser will display Facebook login page
2. Enter your Facebook credentials
3. Choose password manager if prompted

### 4.2 Optimize Settings
1. Go to **Settings** in browser menu
2. Recommended settings for Kindle Oasis 3:
   - Images: **Enabled**
   - JavaScript: **Disabled** (for performance)
   - Videos: **Disabled** (for performance)
   - FB Version: **Lite** (lightest)
   - Cache: **Enabled** (50MB)

## Troubleshooting Installation

### Issue: Extensions folder doesn't exist
**Solution**: Create it manually
```bash
# Via USB (mount first)
mkdir /Volumes/Kindle/extensions/

# Or via SSH
ssh root@192.168.1.X "mkdir -p /mnt/us/extensions"
```

### Issue: Kual doesn't show new extension
**Solution**: 
1. Reboot Kindle
2. Check file permissions: `chmod 755 /mnt/us/extensions/facebook_browser`
3. Verify `menu.json` exists and is valid JSON

### Issue: "Connection refused" when connecting SSH
**Solution**:
1. Ensure Kindle is on same WiFi network
2. Find Kindle IP: **Menu** → **Settings** → **Device Info** → **WiFi Networks**
3. Verify SSH is enabled (may require additional jailbreak packages)

### Issue: Space issues ("Device full")
**Solution**: Free up space
```bash
# Via SSH
rm -rf /mnt/us/extensions/facebook_browser/.cache/*
rm -rf /var/log/*.log
```

## Uninstallation

To remove the Facebook Browser:

1. **Via USB**
   ```bash
   rm -rf /Volumes/Kindle/extensions/facebook_browser/
   ```

2. **Via SSH**
   ```bash
   ssh root@192.168.1.X "rm -rf /mnt/us/extensions/facebook_browser"
   ```

3. **Reboot Kindle**

## Next Steps

- See [USAGE.md](USAGE.md) for how to use the browser
- See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common issues
- Check [DEVELOPMENT.md](DEVELOPMENT.md) if you want to contribute

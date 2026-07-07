#!/bin/sh

# Kindle Oasis 3 Facebook Browser Launcher
# Part of kindle_patch_browser project

set -e

# Configuration
BASE_DIR="/mnt/us/extensions/facebook_browser"
PYTHON_DIR="$BASE_DIR/python"
C_BROWSER="$BASE_DIR/bin/browser"
LOG_FILE="/var/log/facebook_browser.log"
PID_FILE="/var/run/facebook_browser.pid"

# Colors for terminal output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Log function
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> "$LOG_FILE"
}

# Error handling
error_exit() {
    echo -e "${RED}Error: $1${NC}"
    log "ERROR: $1"
    exit 1
}

# Success message
success() {
    echo -e "${GREEN}✓ $1${NC}"
    log "SUCCESS: $1"
}

# Check dependencies
check_deps() {
    log "Checking dependencies..."
    
    # Check for Python
    if command -v python &> /dev/null; then
        PYTHON_VERSION=$(python --version 2>&1 | awk '{print $2}')
        success "Python found: $PYTHON_VERSION"
    else
        error_exit "Python not found. Please install Python on your Kindle."
    fi
    
    # Check for curl or wget
    if command -v curl &> /dev/null; then
        success "curl found"
    elif command -v wget &> /dev/null; then
        success "wget found"
    else
        error_exit "Neither curl nor wget found. Please install one of them."
    fi
}

# Initialize browser
init_browser() {
    log "Initializing browser..."
    
    # Create directories if they don't exist
    mkdir -p "$BASE_DIR/data"
    mkdir -p "$BASE_DIR/cache"
    mkdir -p "$BASE_DIR/cookies"
    
    # Set proper permissions
    chmod 755 "$BASE_DIR/data"
    chmod 755 "$BASE_DIR/cache"
    chmod 755 "$BASE_DIR/cookies"
    
    success "Browser directories initialized"
}

# Start browser process
start_browser() {
    log "Starting Facebook browser..."
    
    # Check if already running
    if [ -f "$PID_FILE" ]; then
        OLD_PID=$(cat "$PID_FILE")
        if kill -0 "$OLD_PID" 2>/dev/null; then
            log "Browser already running with PID $OLD_PID"
            return 0
        fi
    fi
    
    # Use C browser if available, otherwise fall back to Python
    if [ -x "$C_BROWSER" ]; then
        log "Starting C-based browser"
        "$C_BROWSER" &
        echo $! > "$PID_FILE"
        success "C browser started (PID: $!)"
    elif [ -f "$PYTHON_DIR/main.py" ]; then
        log "Starting Python browser wrapper"
        cd "$PYTHON_DIR"
        python main.py &
        echo $! > "$PID_FILE"
        success "Python browser started (PID: $!)"
    else
        error_exit "No browser executable found"
    fi
}

# Main execution
main() {
    echo "═══════════════════════════════════════════════"
    echo "  Facebook Browser for Kindle Oasis 3"
    echo "═══════════════════════════════════════════════"
    echo ""
    
    log "Script started"
    
    check_deps
    init_browser
    start_browser
    
    echo ""
    echo -e "${GREEN}Browser launching...${NC}"
    echo "Press HOME button to return to Kual"
    echo ""
    
    log "Script completed successfully"
}

# Execute
main "$@"

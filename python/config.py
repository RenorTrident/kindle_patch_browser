#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Browser Configuration - Manages all configuration settings
"""

import json
import logging
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class BrowserConfig:
    """Manages browser configuration settings"""
    
    # Default configuration
    DEFAULT_CONFIG = {
        'facebook_version': 'lite',  # lite, mobile, touch, www
        'user_agent': None,  # Auto-detected
        'verify_ssl': True,
        'request_timeout': 30,
        'cache_enabled': True,
        'cache_size_mb': 50,
        'cookies_enabled': True,
        'javascript_enabled': False,  # Disabled for performance
        'images_enabled': True,
        'auto_play_video': False,
        'screen_width': 1680,
        'screen_height': 1264,
        'font_size': 'medium',
    }
    
    def __init__(self, config_file: Optional[str] = None):
        """Initialize configuration
        
        Args:
            config_file: Path to config file, uses default if not specified
        """
        self.config = self.DEFAULT_CONFIG.copy()
        self.config_file = config_file or self._get_default_config_path()
        
        # Load from file if exists
        if self.config_file and Path(self.config_file).exists():
            self._load_config()
        else:
            logger.info("Using default configuration")
        
        logger.info(f"Configuration initialized: {self.config}")
    
    def _get_default_config_path(self) -> str:
        """Get default configuration file path
        
        Returns:
            Path to default config file
        """
        paths = [
            '/mnt/us/.facebook_browser/config.json',
            '/mnt/us/extensions/facebook_browser/config.json',
            '/etc/facebook_browser/config.json',
        ]
        
        for path in paths:
            if Path(path).exists():
                return path
        
        return paths[0]  # Default location
    
    def _load_config(self):
        """Load configuration from file"""
        try:
            logger.info(f"Loading configuration from: {self.config_file}")
            with open(self.config_file, 'r') as f:
                file_config = json.load(f)
                self.config.update(file_config)
                logger.info("Configuration loaded successfully")
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file: {e}")
        except IOError as e:
            logger.error(f"Error reading config file: {e}")
    
    def save_config(self):
        """Save configuration to file"""
        try:
            config_path = Path(self.config_file)
            config_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(self.config_file, 'w') as f:
                json.dump(self.config, f, indent=2)
                logger.info(f"Configuration saved to: {self.config_file}")
        except IOError as e:
            logger.error(f"Error saving config file: {e}")
    
    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value
        
        Args:
            key: Configuration key
            default: Default value if key not found
            
        Returns:
            Configuration value
        """
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any):
        """Set configuration value
        
        Args:
            key: Configuration key
            value: Value to set
        """
        self.config[key] = value
        logger.debug(f"Config set: {key} = {value}")
    
    def update(self, updates: Dict[str, Any]):
        """Update multiple configuration values
        
        Args:
            updates: Dictionary of configuration updates
        """
        self.config.update(updates)
        logger.debug(f"Config updated with: {updates}")
    
    def get_device_info(self) -> Dict[str, Any]:
        """Get device information
        
        Returns:
            Device info dictionary
        """
        return {
            'device': 'Kindle Oasis 3',
            'screen_width': self.get('screen_width'),
            'screen_height': self.get('screen_height'),
            'memory': self._get_memory_info(),
        }
    
    def _get_memory_info(self) -> Dict[str, int]:
        """Get memory information
        
        Returns:
            Memory info dictionary
        """
        try:
            with open('/proc/meminfo', 'r') as f:
                lines = f.readlines()
                mem_info = {}
                for line in lines:
                    if ':' in line:
                        key, value = line.split(':')
                        mem_info[key.strip()] = int(value.split()[0])
                return mem_info
        except Exception as e:
            logger.warning(f"Could not read memory info: {e}")
            return {}
    
    def validate(self) -> bool:
        """Validate configuration
        
        Returns:
            True if configuration is valid
        """
        required_keys = ['facebook_version']
        for key in required_keys:
            if key not in self.config:
                logger.error(f"Missing required config key: {key}")
                return False
        
        valid_versions = ['lite', 'mobile', 'touch', 'www']
        if self.config['facebook_version'] not in valid_versions:
            logger.error(f"Invalid facebook_version: {self.config['facebook_version']}")
            return False
        
        return True

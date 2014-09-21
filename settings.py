# Scrapy settings for cne project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import os



DATABASE = { 
    'drivername': 'postgres',
    'host': os.environ.get('CNE_DB_HOST', 'localhost'),
    'port': os.environ.get('CNE_DB_PORT', 5432),
    'username': os.environ.get('CNE_DB_USER', 'scrapy'),
    'password': os.environ.get('CNE_DB_PASSWORD', 'scrapy'),
    'database': os.environ.get('CNE_DB_NAME', 'scrapy')
}


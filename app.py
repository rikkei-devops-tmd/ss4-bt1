import os
import sys

def get_system_info():
    return {
        "status": "online",
        "service": "it209-devops-service",
        "environment": "local-development"
    }

if __name__ == "__main__":
    info = get_system_info()
    print(f"Service: {info['service']}, Status: {info['status']}")

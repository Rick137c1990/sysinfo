import platform
import socket
import psutil


def get_os_name()-> str:
    """Return operating system name."""
    return platform.system()

def get_python_version()-> str:
    """Return python version."""
    return platform.python_version()

def get_hostname()-> str:
    """Return hostname."""
    return platform.node()

def get_kernel()-> str:
    """Return kernel version."""
    return platform.release()

def get_architecture()-> str:
    """Return architecture."""
    return str(platform.architecture()[0])

def get_processor()-> str:
    """Return processor version."""
    return platform.processor()

def bytes_to_gb(value: int) -> str:
    return f"{value / (1024 ** 3):.2f} GB"

def get_memory_info() -> dict:
    """Return ram info: total, available, used, free, percent"""
    memory = psutil.virtual_memory()

    return {
        "Total": bytes_to_gb(memory.total),
        "Available": bytes_to_gb(memory.available),
        "Used": bytes_to_gb(memory.used),
        "Free": bytes_to_gb(memory.free),
        "Percent": str(memory.percent) + "%"
    }

def get_host_ip()-> str:
    """Return ip address."""
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 80))
        return s.getsockname()[0]
    finally:
        s.close()

def get_info()-> dict:
    """Return all system info."""
    return  {
        "System": {
            "OS": get_os_name(),
            "Hostname": get_hostname(),
            "Kernel": get_kernel(),
            "Architecture": get_architecture(),
        },
        "Python": {
            "Version": get_python_version(),
        },
        "Network": {
            "IP": get_host_ip(),
        },
        "CPU": {
            "CPU": get_processor(),
        },
        "RAM": get_memory_info(),
}





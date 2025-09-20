import os
import shutil
import psutil
from utils import format_bytes

def execute_command(command):
    parts = command.split()
    cmd = parts[0]
    args = parts[1:]

    try:
        if cmd == "pwd":
            print(os.getcwd())

        elif cmd == "ls":
            print("\n".join(os.listdir(os.getcwd())))

        elif cmd == "cd":
            if args:
                os.chdir(args[0])
            else:
                print("Usage: cd <directory>")

        elif cmd == "mkdir":
            if args:
                os.mkdir(args[0])
            else:
                print("Usage: mkdir <dirname>")

        elif cmd == "rm":
            if args:
                target = args[0]
                if os.path.isdir(target):
                    shutil.rmtree(target)
                elif os.path.isfile(target):
                    os.remove(target)
                else:
                    print("No such file or directory")
            else:
                print("Usage: rm <file/dir>")

        elif cmd == "cpu":
            print(f"CPU Usage: {psutil.cpu_percent()}%")

        elif cmd == "mem":
            memory = psutil.virtual_memory()
            print(f"Memory Usage: {format_bytes(memory.used)} / {format_bytes(memory.total)}")

        elif cmd == "ps":
            for proc in psutil.process_iter(['pid', 'name']):
                print(f"{proc.info['pid']} - {proc.info['name']}")

        else:
            print(f"Unknown command: {cmd}")
    except Exception as e:
        print(f"❌ Command failed: {e}")

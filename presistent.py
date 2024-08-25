import os
import time
import shutil

def install_agent():
    # Install agent in a hidden or protected directory
    protected_dir = '/protected_agent'
    if not os.path.exists(protected_dir):
        os.mkdir(protected_dir)
    
    agent_file = os.path.join(protected_dir, 'agent.py')
    if not os.path.exists(agent_file):
        with open(agent_file, 'w') as f:
            f.write("# Agent code here\nprint('Agent running')")

def run_agent():
    # Periodically check for tampering or system format
    while True:
        if system_formatted():
            reinstall_agent()
        time.sleep(3600)  # Check every hour

def system_formatted():
    # Logic to detect if the system has been formatted
    # For simplicity, we'll just check if the protected directory still exists
    return not os.path.exists('/protected_agent')

def reinstall_agent():
    # Reinstall the agent if the system has been formatted
    install_agent()
    print("Reinstalled agent after system format.")

def start_agent():
    # Execute the agent code
    protected_dir = '/protected_agent'
    agent_file = os.path.join(protected_dir, 'agent.py')
    if os.path.exists(agent_file):
        exec(open(agent_file).read())

install_agent()
run_agent()

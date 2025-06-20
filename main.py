from scheduler import run_scheduling
from memory_allocation import run_memory_allocation
from shared_memory_ipc import run_ipc_demo
from deadlock_detection import run_deadlock_detection

def main():
    while True:
        print("\n--- Memory Allocation Visualizer ---")
        print("1. Run Scheduling Algorithms")
        print("2. Run Memory Allocation Strategies")
        print("3. Run Deadlock Detection")
        print("4. Run Shared Memory IPC Simulation")
        print("5. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == '1':
            run_scheduling()
        elif choice == '2':
            run_memory_allocation()
        elif choice == '3':
            run_deadlock_detection()
        elif choice == '4':
            run_ipc_demo()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()

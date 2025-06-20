def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                allocation[i] = j
                blocks[j] -= processes[i]
                break
    return allocation

def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    for i in range(len(processes)):
        best_idx = -1
        for j in range(len(blocks)):
            if blocks[j] >= processes[i]:
                if best_idx == -1 or blocks[j] < blocks[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            blocks[best_idx] -= processes[i]
    return allocation

def run_memory_allocation():
    blocks = list(map(int, input("Enter memory block sizes: ").split()))
    processes = list(map(int, input("Enter process memory needs: ").split()))
    print("1. First Fit\n2. Best Fit")
    ch = input("Choose strategy: ")
    if ch == '1':
        allocation = first_fit(blocks[:], processes)
    elif ch == '2':
        allocation = best_fit(blocks[:], processes)
    else:
        print("Invalid choice.")
        return

    print("\nProcess No.\tProcess Size\tBlock No.")
    for i in range(len(processes)):
        print(f"{i + 1}\t\t{processes[i]}\t\t{allocation[i] + 1 if allocation[i] != -1 else 'Not Allocated'}")

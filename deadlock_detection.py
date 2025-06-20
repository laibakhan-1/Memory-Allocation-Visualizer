def is_safe(processes, avail, max_demand, alloc):
    n = len(processes)
    m = len(avail)
    need = [[max_demand[i][j] - alloc[i][j] for j in range(m)] for i in range(n)]
    finish = [False] * n
    safe_seq = []
    work = avail[:]

    while len(safe_seq) < n:
        allocated = False
        for i in range(n):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(m)):
                for j in range(m):
                    work[j] += alloc[i][j]
                safe_seq.append(processes[i])
                finish[i] = True
                allocated = True
        if not allocated:
            return False, []
    return True, safe_seq

def run_deadlock_detection():
    n = int(input("Enter number of processes: "))
    m = int(input("Enter number of resources: "))
    processes = [f'P{i}' for i in range(n)]

    print("Enter allocation matrix:")
    alloc = [list(map(int, input().split())) for _ in range(n)]
    print("Enter maximum demand matrix:")
    max_demand = [list(map(int, input().split())) for _ in range(n)]
    avail = list(map(int, input("Enter available resources: ").split()))

    safe, seq = is_safe(processes, avail, max_demand, alloc)
    if safe:
        print("System is in a safe state. Safe sequence is:", " -> ".join(seq))
    else:
        print("System is in DEADLOCK.")

import matplotlib.pyplot as plt
from gantt_chart import draw_gantt_chart

def fcfs(processes):
    processes.sort(key=lambda x: x['arrival'])
    time = 0
    chart = []
    for p in processes:
        start = max(time, p['arrival'])
        end = start + p['burst']
        chart.append((p['id'], start, end))
        time = end
    return chart

def sjf(processes):
    processes.sort(key=lambda x: (x['arrival'], x['burst']))
    time = 0
    chart = []
    ready_queue = []
    idx = 0
    n = len(processes)
    completed = 0

    while completed < n:
        while idx < n and processes[idx]['arrival'] <= time:
            ready_queue.append(processes[idx])
            idx += 1
        if ready_queue:
            ready_queue.sort(key=lambda x: x['burst'])
            current = ready_queue.pop(0)
            start = time
            end = start + current['burst']
            chart.append((current['id'], start, end))
            time = end
            completed += 1
        else:
            time += 1
    return chart

def round_robin(processes, quantum):
    from collections import deque
    queue = deque()
    time = 0
    chart = []
    idx = 0
    n = len(processes)
    remaining = {p['id']: p['burst'] for p in processes}
    arrival_dict = {p['id']: p['arrival'] for p in processes}
    queue.extend([p for p in processes if p['arrival'] == 0])
    idx = len(queue)

    while queue or any(remaining.values()):
        if not queue:
            time += 1
            queue.extend([p for p in processes if p['arrival'] == time])
            continue
        current = queue.popleft()
        pid = current['id']
        start = time
        exec_time = min(quantum, remaining[pid])
        time += exec_time
        remaining[pid] -= exec_time
        chart.append((pid, start, time))
        if remaining[pid] > 0:
            queue.append(current)
        queue.extend([p for p in processes if arrival_dict[p['id']] > start and arrival_dict[p['id']] <= time])
    return chart

def run_scheduling():
    processes = []
    n = int(input("Enter number of processes: "))
    for i in range(n):
        pid = input(f"Process ID {i+1}: ")
        arrival = int(input("Arrival Time: "))
        burst = int(input("Burst Time: "))
        processes.append({'id': pid, 'arrival': arrival, 'burst': burst})

    print("\n1. FCFS\n2. SJF\n3. Round Robin")
    ch = input("Choose scheduling algorithm: ")
    if ch == '1':
        chart = fcfs(processes)
    elif ch == '2':
        chart = sjf(processes)
    elif ch == '3':
        q = int(input("Enter Time Quantum: "))
        chart = round_robin(processes, q)
    else:
        print("Invalid choice.")
        return

    draw_gantt_chart(chart, title="Gantt Chart")

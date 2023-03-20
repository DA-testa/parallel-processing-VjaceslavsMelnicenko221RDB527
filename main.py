# python3

def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, create the output pairs
    thr = [(i, 0) for i in range(n)]
    for i in range(m):
        t = data[i]
        thr_i, st_te = min(thr, key=lambda x: x[1])
        output.append((thr_i, st_te))
        thr[thr_i] = (thr_i, st_te+t) 
    return output

def main():
  
    n, m = map(int, input().split())

    
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_idx, start_time in result:
        print(thread_idx, start_time)

if name == "main":
    main()

# python3

def parallel_processing(n, m, data):
    output = []
    tr = [(i, 0) for i in range(n)]
    for i in range(m):
        t = data[i]
        t_idx, st_te = min(tr, key=lambda x: x[1])
        output.append((t_idx, st_te))
        tr[t_idx] = (t_idx, st_te+t) 
    return output

def main():
    # first line - n and m
    # n - thread count 
    # m - job count
    n, m = map(int, input().split())

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_idx, start_time in result:
        print(thread_idx, start_time)

if __name__ == "__main__":
    main()

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        n = len(servers)
        sorted_servers = sorted(range(n), key=lambda i: (servers[i], i))
        free_time = [0] * n
        
        block_size = int(n ** 0.5) + 1
        num_blocks = (n + block_size - 1) // block_size
        group_min = [0] * num_blocks
        
        ans = []
        t = 0
        
        for j, duration in enumerate(tasks):
            if j > t:
                t = j
                
            earliest_overall = min(group_min)
            if earliest_overall > t:
                t = earliest_overall
                
            chosen_group = 0
            for g in range(num_blocks):
                if group_min[g] <= t:
                    chosen_group = g
                    break
                    
            start = chosen_group * block_size
            end = min(n, start + block_size)
            
            best_pos = start
            for pos in range(start, end):
                if free_time[pos] <= t:
                    best_pos = pos
                    break
                    
            ans.append(sorted_servers[best_pos])
            free_time[best_pos] = t + duration
            group_min[chosen_group] = min(free_time[start:end])
            
        return ans